from fastapi import FastAPI
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

#Importamos los df
df_games = pd.read_csv('archivos csv/games.csv')
df_items = pd.read_csv('archivos csv/items.csv')
df_reviews = pd.read_csv('archivos csv/reviews.csv')
#Este df lo utilizaremos en la funcion de ML
df_games_union = pd.read_csv('archivos csv/games_union_ml.csv')


lista_de_genres = 'Action', 'Casual', 'Indie', 'Simulation', 'Strategy','Free to Play', 'Rpg', 'Sports', 'Adventure', 'Racing','Massively Multiplayer', 'Early Access', 'Animation and Modeling','Video Production', 'Utilities', 'Web Publishing', 'Education','Software Training', 'Design and Illustration', 'Audio Production','Photo Editing', 'Accounting'

#Tenemos que crear las rutas raiz 127.0.0.1:8000 para este puerto
#Primera función
#es importante que le pongamos @ es lo se le llamada decorador, este acompaña o modifica a la funcion que le sigue, en este caso la registra.
@app.get("/playtimegenre/{genero}")
def PlayTimeGenre( genero : str ):

    # Aplanar el género ingresado para que la primera letra sea mayúscula y las demás minúsculas
    genero_aplanado = genero.capitalize()

    # Hacemos un join de las tablas para tener las horas agrupadas a los items
    df_join = df_games.merge(df_items, on='item_id', how='inner')

    # Filtro por genero solicitado
    df_join = df_join.loc[df_join['genres']== genero_aplanado].drop(columns=['release_date'], axis=1)

    #Si no encuentra el valore devuele el mensaje
    if df_join.empty:
            return {"message": f"No se encontraron datos para el género {genero_aplanado}. Por favor seleccione alguno de los siguientes generos: {lista_de_genres}"}

    # Realizo la suma por año 
    suma_por_años = df_join.groupby('year_release')['playtime_forever'].sum()

    # Escojemos el año con la suma más alta
    año_con_mas_horas = suma_por_años.idxmax()

    # Retorno el año con mas horas por genero
    return {f"El año de lanzamiento con más horas jugadas para el Género {genero_aplanado} es" : f"{año_con_mas_horas}"}


#Segunda función
@app.get("/userforgenre/{genero}")
def UserForGenre( genero : str ):

    # Aplanar el género ingresado para que la primera letra sea mayúscula y las demás minúsculas
    genero_aplanado = genero.capitalize()

    # Hacemos un join de las tablas para tener las horas, el usuario agrupadas a los items
    df_join = df_games.merge(df_items, on='item_id', how='inner')

    # Filtro por el genero solicitado
    df_join = df_join.loc[df_join['genres']== genero_aplanado].drop(columns=['release_date'], axis=1)

    #Si no encuentra el valore devuele el mensaje
    if df_join.empty:
        return {"message": f"No se encontraron datos para el género {genero_aplanado}. Por favor seleccione alguno de los siguientes generos: {lista_de_genres}"}

    # Sumo por usuario (ya esta filtrado por el genero). Me crea un df
    suma_por_años = df_join.groupby(['user_id'])['playtime_forever'].sum().reset_index()
    
    # Guardo el nombre del usuario con más horas jugadas en una variable
    user_con_mas_horas = suma_por_años.max()[0]

    # Creo un nuevo df en donde filtro por el usuario con más horas, para poder sacar sus horas por año
    df_join_user = df_join[df_join['user_id'] == user_con_mas_horas].drop(columns=['item_id','user_id','genres'], axis=1)

    # Ahora voy a sumar por año (ya esta filtrado por el usuario). Me crea un df
    suma_por_años = df_join_user.groupby('year_release')['playtime_forever'].sum().reset_index()

    # Conveirto el DataFrame a un diccionario para poder iterarlo
    suma_por_años_dic = suma_por_años.to_dict(orient='records')

    # Crear una lista para poder darle una forma más clara a la respuesta
    año_y_horas = [{"año": i['year_release'], "horas_jugadas": i['playtime_forever']} for i in suma_por_años_dic]

    # Retorno la respuesta en formato JSON
    return {
        f'El usuario con mas horas jugadas para el genero {genero_aplanado} es': f' {user_con_mas_horas} ',
        f'Su historial es': f' {año_y_horas} '
    }


#Tercera función
@app.get("/usersrecommend/{year}")
def UsersRecommend(year : int):

    if year >= 2010 and year <= 2016:
        #filtramos el df por el año, es decir unicamente queremos datos que correspondan a ese año
        df_reviews_filtrado = df_reviews[df_reviews['year'] == year]

        #Filtramos el df que ya esta filtrado, por el analisis sentiment sea 1 o 2
        df_reviews_filtrado = df_reviews_filtrado[df_reviews_filtrado['sentiment_analysis'].isin([1, 2])]

        #Agrupamos por item_id, el conteo de las recomendaciones True
        conteo_recomendacion_por_juego = df_reviews_filtrado.groupby('item_id')['recommend'].sum().reset_index()

        #Hacemos un df en donde ponemos los 3 con más conteo
        top_3_recommended = conteo_recomendacion_por_juego.nlargest(3, 'recommend')

        #Retornamos el Id de los juegos con más recomendaciones por el año
        return {
            f"Top 3 de los id de juegos más recomendados por el año {year}":
            [
                {"puesto 1": f"id = {str(top_3_recommended['item_id'].iloc[0])}"},
                {"puesto 2": f"id = {str(top_3_recommended['item_id'].iloc[1])}"},
                {"puesto 3": f"id = {str(top_3_recommended['item_id'].iloc[2])}"}
            ]
        }
    else:
        return {f'Ingrese un año valido entre 2010 y 2016'}


#Cuarta función
@app.get("/usersnotrecommend/{year}")
def UsersNotRecommend( year : int ):
    if year >= 2010 and year <= 2016:
        #filtramos el df por el año, es decir unicamente queremos datos que correspondan a ese año
        df_reviews_filtrado = df_reviews[df_reviews['year'] == year]

        #Filtramos el df que ya esta filtrado, por el analisis sentiment sea 0
        df_reviews_filtrado = df_reviews_filtrado[df_reviews_filtrado['sentiment_analysis'].isin([0])]

        #Agrupamos por item_id, el conteo de las recomendaciones False, para esto usamos una función lambda en donde usamos el '~', que se lo usa para negar el True, ya que no es correcto usar .sum(False), entonces utilizamos la negacion de True(No True) que es equivalente a False
        conteo_recomendacion_por_juego = df_reviews_filtrado.groupby('item_id')['recommend'].apply(lambda x: (~x).sum()).reset_index()

        #Hacemos un df en donde ponemos los 3 con más conteo de False
        top_3_recommended = conteo_recomendacion_por_juego.nlargest(3, 'recommend')

        #Retornamos el Id de los juegos con menos recomendaciones por el año
        return {
            f"Top 3 de los id de juegos menos recomendados por el año {year}":
            [
                {"puesto 1": f"id = {str(top_3_recommended['item_id'].iloc[0])}"},
                {"puesto 2": f"id = {str(top_3_recommended['item_id'].iloc[1])}"},
                {"puesto 3": f"id = {str(top_3_recommended['item_id'].iloc[2])}"}
            ]
        }
    else:
        return {f'Ingrese un año vaido entre 2010 y 2016'}

#Quinta función
@app.get("/sentimentanalysis/{year}")
def sentiment_analysis( year : int ):
    
    if year >= 2010 and year <= 2016:
        #La funcion debe estar según el año de lanzamiento, primero filtramos el df por el año
        df_games_filtrado_año = df_games[df_games['year_release'] == year]

        #Hacemos un inner join con dos df, el de 'games' que ya esta filtrado por la fecha que necesitamos y el df de 'reviews' de cual necesitamos la informacion del sentiment_analysis
        df_join_analysis = df_games_filtrado_año.merge(df_reviews, on='item_id', how='inner')

        #Quitamos columas innesesarias que no utilizaremos
        df_join_analysis = df_join_analysis[['item_id', 'year_release', 'user_id','sentiment_analysis']]

        #Hacemos un conteo de sentiment_analysis
        conteo_sentiment_analysis = df_join_analysis['sentiment_analysis'].value_counts()

        #Retornamos la cantidad de registros de reseñas de usuarios, ya sea negativo, neutro o positivo por el año de lanzamiento del juego
        return {
                f'La cantidad de registros de reseñas de usuarios por el año de lanzamiento {year} son':
                {
                    'Negativos' : f'{conteo_sentiment_analysis[0]}', 'Neutros' : f'{conteo_sentiment_analysis[1]}', 'Positivos' : f'{conteo_sentiment_analysis[2]}'
                }
                }
    else:
        return {f'Ingrese un año vaido entre 2010 y 2016'}


#Función de ML
@app.get("/recomendacionjuego/{id}")
def recomendacion_juego( id : int ):
    try:
        #Filtra el DataFrame para obtener los juegos del género de referencia. Lo guardamos en una variable llamada genre_reference:
        genre_reference = df_games_union.loc[df_games_union['item_id'] == id, 'genres'].iloc[0]
        df_filtered = df_games_union[df_games_union['genres'] == genre_reference]

        #Creo una matriz de características donde cada fila representa un juego y cada columna representa un tags. Si un juego pertenece a un tags, el valor en la columna correspondiente es 1; de lo contrario, es 0. Esto se hace utilizando la función pivot_table en pandas:
        df_games_encoded = pd.get_dummies(df_filtered, columns=['tags'], dtype=int)

        #eliminamos columnas insignificantes
        df_games_encoded.drop(columns=['genres'], axis=1, inplace=True)

        #esta es la parte pesada, tenemos que calcular la similitud del coseno
        cosine_sim = cosine_similarity(df_games_encoded, df_games_encoded)

        # guardamos el indice del juego de referencia
        reference_game_index = df_filtered.index.values[0]

        # Obtenemos las similitudes del juego de referencia con otros juegos
        similarities = cosine_sim[reference_game_index]

        # Enumeramos las similitudes junto con los índices de los juegos
        similar_games = list(enumerate(similarities))

        # Ordenamos la lista de juegos similares por similitud en orden descendente
        similar_games_sorted = sorted(similar_games, key=lambda x: x[1], reverse=True)

        # Excluhimos el juego de referencia y toma los 5 juegos más similares
        top_similar_games = similar_games_sorted[1:6]

        # Obtenemos los índices de los juegos recomendados
        recommended_game_indices = [game[0] for game in top_similar_games]

        return {
            'Top 5 de id de los juegos más recomendados similares al que ingreso' : f'{recommended_game_indices}'
        }
    except Exception:
        return 'Por favor ingrese un id valido'


