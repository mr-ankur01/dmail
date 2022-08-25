import requests
import json


def get_token(address: str, password: str):
    try:
        body = {
                'address':address,
                'password': password
            }
        url='https://api.mail.tm/token'
        
        headers = {
                'content-type': 'application/ld+json',
            }
        req = requests.post(
                url=url, 
                data=json.dumps(body),
                headers=headers
                ).json()
        id =req.get('id')
        token =req.get('token')
        return token   
    except Exception as e:
        print('token: ',e) 

