# Principios_Solid_DAS
Actividad individual: Principios SOLID

Toma como referencia el archivo llamado movie_fetcher.py y realiza las siguientes tareas:

Analiza el funcionamiento del script.
- ¿Cual es su entrada?
- - http://www.imdb.com/chart/top Esta url es la entreda, te dirige a una lista top 250 películas de IMDB
- ¿Que procesamiento esta haciendo?
- - Hace una petición a la url. Esta retorna información acerca de las películas en la lista. Se hace un proceso de limpieza de datos xml para al final regresar la lista en formato CSV.
- ¿Cual es su salida?
- - Una lista de películas en formato CSV
 Una vez identificado el funcionamiento, refactoriza el script en diferentes metodos o clases de tal manera que sea mas facil de leer y de entender.
La refactorizacion debe seguir los principios de SOLID vistos en clase.
