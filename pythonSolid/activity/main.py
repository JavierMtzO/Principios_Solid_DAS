from requester import url_connection
from scrapper import get_scrapper, scrap
from compositioner import create_movie_composition
from csv_creator import create_movies_csv

def main():
    # Requesting data from http://www.imdb.com/chart/top
    url = 'http://www.imdb.com/chart/top'
    response = url_connection(url)
    parser_type = 'lxml'
    soup = get_scrapper(response, parser_type)
    # Scrapping information as a xml file
    movies, links, crew, ratings, votes = scrap(soup)
    # Composing movie list
    movies = create_movie_composition(movies, links, crew, ratings, votes)
    # Creating csv file with the results
    filename = "movie_results.csv"
    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    create_movies_csv(fields, movies, filename)


if __name__ == '__main__':
    main()

'''
En esta actividad se aplicaron los siguientes principios de SOLID:
- S: A module for only one thing
    Tenemos un archivo main el cuál hace llamar todas las funcionalidades con sus respectivos parámetros.
    Haciendo un modulo de repartición de funcionalidades.
- D: Dependency Inversion
    Este principio aplica en la distribución de funcionalidades junto con sus librerías que necesitan importar. 
    Las 4 librerías que se importaban en este main, se dividieron en los 4 archivos creados con sus funcionalidades.
- O: Extendible code
    Las funcionalidades fueron divididas para lograr este principio de SOLID. Ya que si se necesitara hacer lo mismo
    con otro link, se pudiera realizar mandando los parámetros deseados en vez de replicar el código de la funcionalidad.
'''