<h1 align="center" style="font-size: 36px;">Proyecto Individual Henry</h1>


Este proyecto es el resultado de un trabajo práctico integrador realizado como parte del Bootcamp de Data Science de SoyHenry. El objetivo principal de este proyecto es crear un sistema de recomendación de videojuegos para usuarios de Steam, una plataforma multinacional de videojuegos.

<p align="center">
  <img src="/data/portada.jpg">
</p>


## Introducción
Tenemos que ponernos en contexto, imagina trabajar como Data Scientist en Steam y enfrentarte al desafío de crear un sistema de recomendación de videojuegos para sus usuarios. Sin embargo, te encuentras con un obstáculo importante: la calidad y madurez de los datos disponibles es muy baja. Los datos están anidados, en formato crudo y no hay procesos automatizados para la actualización de nuevos productos.

A pesar de estos desafíos, estás decidido a superarlos y crear un MVP (Minimum Viable Product) para cumplir con el proyecto. Este README proporcionará una visión general de cómo abordaste este proyecto desde cero y las soluciones que implementaste.

## Objetivos

El objetivo principal de este proyecto es desarrollar un sistema de recomendación de videojuegos que pueda proporcionar a los usuarios de Steam sugerencias personalizadas basadas en sus preferencias y comportamientos pasados.

El sistema de recomendación que realizé es un sistema de recomendación de item a item, es decir, de acuerdo a un id del juego que ingrese a la función, esta te retornará una lista con los id de los cinco juegos recomendados.

## Proceso
Para lograr este objetivo, se llevaron a cabo los siguientes pasos clave:

1. **Exploración de Datos**: Se exploraron los datos disponibles para comprender su estructura y calidad. Se identificaron problemas y desafíos relacionados con la calidad de los datos.

2. **Limpieza y Transformación de Datos**: Durante esta etapa, se realizaron tareas de limpieza de datos exhaustivas para abordar problemas como datos anidados, valores nulos y otros problemas de calidad de datos. Sin embargo, uno de los desafíos clave fue la identificación y gestión de valores críticos que eran fundamentales para el proyecto. 

   - **Identificación de Valores Críticos**: Se llevaron a cabo análisis detallados para identificar valores clave que eran críticos para el proyecto. Estos valores eran esenciales para la precisión del sistema de recomendación y su eliminación habría resultado en una pérdida significativa de información relevante.

   - **Criterios de Conservación**: Se establecieron criterios sólidos para determinar cuándo era apropiado conservar y transformar valores críticos en lugar de eliminarlos. Estos criterios se basaron en la importancia y relevancia de los datos para el objetivo del proyecto.

   - **Transformación Controlada**: Los valores críticos se transformaron de manera controlada para garantizar que sigan siendo útiles y aplicables para su uso en el sistema de recomendación. Se aplicaron técnicas de interpolación, extrapolación y otras transformaciones específicas según corresponda.

   - **Gestión de Valores Nulos**: Se abordaron los valores nulos mediante la imputación de datos utilizando estrategias como la imputación por media, moda ou otros criterios.

   - **Normalización y Estandarización**: Se realizó la normalización y estandarización de datos para garantizar la coherencia y comparabilidad entre diferentes variables, ya que los dataset se relacionan entre si, comparten información que es clave. Una mala normalización impolica problemas en nuestras funciones y sistema.


Esta etapa fue esencial para garantizar que los datos fueran adecuados para su procesamiento posterior y que se mantuviera la integridad de los valores críticos, preservando así información valiosa y relevante para el sistema de recomendación.

3. **Desarrollo del Modelo de Recomendación**: Se seleccionó y desarrolló un modelo de recomendación adecuado, como filtrado colaborativo o sistemas de recomendación basados en contenido.

4. **Evaluación del Modelo**: Se evaluó el rendimiento del modelo utilizando métricas apropiadas, como precisión, recuperación, F1-score u otras métricas relevantes.

5. **Despliegue del MVP**: Se creó un MVP del sistema de recomendación que permitió a los usuarios recibir recomendaciones personalizadas.

### Desarrollo de la API

Proponemos disponibilizar los datos de la empresa utilizando el framework FastAPI. Creamos las siguientes funciones para los endpoints que se consumirán en la API:

- `PlayTimeGenre(genero: str)`: Devuelve el año con más horas jugadas para un género dado.
- `UserForGenre(genero: str)`: Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
- `UsersRecommend(año: int)`: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.
- `UsersNotRecommend(año: int)`: Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado.
- `sentiment_analysis(año: int)`: Según el año de lanzamiento, devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentran categorizados con un análisis de sentimiento.

Estos endpoints permitirán a los usuarios obtener recomendaciones personalizadas, consultar datos relacionados con el tiempo de juego y el sentimiento de las reseñas, y obtener información valiosa sobre juegos recomendados y no recomendados.
## Video de Demostración del Proyecto

**Título del Video:** "Demostración del Proyecto: Sistema de Recomendación de Videojuegos para Usuarios de Steam"

**Descripción del Video:**
Este video ofrece una breve explicación de nuestro proyecto, desde la limpieza de datos hasta la implementación de un sistema de recomendación de videojuegos para usuarios de Steam. Abordaremos sobre los criterios utilizados, el análisis exploratorio de datos y cómo funciona la API. ¡Descúbrelo todo en este video!

**Enlace al Video:** [link](https://drive.google.com/drive/folders/1IHyxwrSCUg8iVDqoXQFzB8G3O8qAMiLb?usp=sharing)

## Estructura del Repositorio

- `__pycache__/`: Es un directorio que Python utiliza para almacenar archivos de caché de código fuente compilado.
- `archivos csv/`: Contiene los datos utilizados y consumidos por FastAPI.
- `.gitignore/`: Es fundamental en un repositorio Git. Ya que sirve para especificar qué archivos o directorios deben ser ignorados por Git
- `main.py/`:  Este es el archivo principal del proyecto. Contiene el código principal de la aplicación FastAPI. Es donde estan definidas las rutas y las funciones para manejar las solicitudes HTTP y ejecutar la lógica de la aplicación.
- `requirements.txt`: Este archivo enumera las dependencias del proyecto, es decir, las bibliotecas de Python que la aplicación necesita para funcionar correctamente.
- `EDA _y_ETL.ipynb`: Archivo en donde esta el codigo y el paso a paso de como fui haciendo el proceso de EDA y de ETL.
-  `sentiment_analysis.ipynb`: Archivo en donde realizo la creación del modelo de analisis de sentimiento. Para la creación de este archivo probé y comparé resultados con otras librerias como 'textblob' pero según mi criterio me quede con 'nltk', ya que returnaba resultados un poco más precisos y acordes.
-  `creación_de_las_funciones.ipynb`: En este archivo mustro de una forma máss limpia y ordenada las funciones. Esta el resultado final pero antes de llegar a los resultados fueron muchas pruebas y errores.
-  `modelo_de_ML.ipynb`: Aqui se almacena el codigo de la creación del codigo de la función del modelo de Machine Learning. Analicé diversas formas de poder desarrollar el modelo y al final me decanté por el modelo de recomendación a base de la similitud del coseno.
- `Datasets y archivos originales`: Esta carpeta contiene los archivos originales que se proporcionaron para la realización del proyecto. ¡Dale un vistazo!

## Material de origen

* Puedes acceder al repositorio donde estan las consignas haciendo click [aquí](https://github.com/soyHenry/PI_ML_OPS/tree/FT)
* Este [repositorio](https://github.com/HX-FNegrete/render-fastapi-tutorial) explica como utilizar levantar un proyecto de data en general.

## Contribución

Este proyecto es parte del trabajo práctico integrador realizado en el Bootcamp de Data Science de SoyHenry y no acepta contribuciones externas en este momento.


## Contacto
- LinkedIn : [Lucas Santos Oliveira](www.linkedin.com/in/lucas-santosoliveira10)
- Correo electronico : lucas-santosoliveira@hotmail.com
