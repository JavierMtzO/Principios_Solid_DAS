import requests

def url_connection(url: str):
    response = requests.get(url)
    return response