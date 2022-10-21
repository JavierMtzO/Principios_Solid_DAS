from bs4 import BeautifulSoup

def get_scrapper(response, parser_type: str):
    soup = BeautifulSoup(response.text, parser_type)
    return soup

def scrap(soup: BeautifulSoup):
    # Get information from xml soup
    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
    votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

    return movies, links, crew, ratings, votes