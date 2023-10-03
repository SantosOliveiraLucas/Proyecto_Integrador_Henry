# Proyecto_Integrador_Henry
Este proyecto es el resultado de un trabajo práctico integrador realizado como parte del Bootcamp de Data Science de SoyHenry. El objetivo principal de este proyecto es crear un sistema de recomendación de videojuegos para usuarios de Steam, una plataforma multinacional de videojuegos.

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

## Estructura del Repositorio

- `notebooks/`: Contiene los cuadernos Jupyter utilizados para la exploración de datos, el desarrollo del modelo y la evaluación.
- `data/`: Contiene los datos utilizados en el proyecto.
- `src/`: Contiene el código fuente del sistema de recomendación y la API.
- `docs/`: Documentación adicional y recursos relacionados con el proyecto.
- `requirements.txt`: Lista de dependencias del proyecto.

## Uso

Si deseas utilizar el sistema de recomendación, sigue las instrucciones en la carpeta `src/` para

Si deseas utilizar el sistema de recomendación, sigue las instrucciones en la carpeta `src/` para implementar y ejecutar el código.

## Contribución

Este proyecto es parte del trabajo práctico integrador realizado en el Bootcamp de Data Science de SoyHenry y no acepta contribuciones externas en este momento.

## Licencia

Este proyecto se publica bajo la Licencia [Nombre de la Licencia]. Consulta el archivo LICENSE.md para obtener más detalles.

## Contacto
