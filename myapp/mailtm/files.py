import requests

def get_file(downloadUrl: str,token:str):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/ld+json',
    }
    
    res = requests.get(url=f'https://api.mail.tm{downloadUrl}',headers=headers)
    return res.content
    