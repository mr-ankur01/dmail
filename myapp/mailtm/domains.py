import requests

def get(page: int = 1):
 
    url = 'https://api.mail.tm/domains'
    params = {
        'page': page
    }
    response = requests.get(url=url, params=params)
    domain=response.json()["hydra:member"][0]['domain']
    return '@'+domain