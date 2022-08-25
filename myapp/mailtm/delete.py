import requests

def delete_msg(id: str , token: str):
    headers = {
                'Authorization': f'Bearer {token}',
                'accept': 'application/ld+json',
            }
    res = requests.delete(url=f'https://api.mail.tm/messages/{id}',headers=headers)
    return res

