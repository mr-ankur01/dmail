from . import BASE_URL
import requests

def get_msgs(token):
    try:

        url ='https://api.mail.tm/messages'
        params = {
                'page': 1,
            }
        headers = {
                'Authorization': f'Bearer {token}',
                'accept': 'application/ld+json',
            }
        response = requests.get(
                url=url,
                params=params,
                headers=headers
            ).json()
        return response
    except Exception as e:
        print('msgs. get_msgs: ',e)


def get_msg(id: str , token: str):
    try:

        url = f'https://api.mail.tm/messages/{id}'
        params = {
                'page': 1,
            }
        headers = {
                'Authorization': f'Bearer {token}',
                'accept': 'application/ld+json',
            }
        response = requests.get(
                url=url,
                params=params,
                headers=headers
            ).json()
        return response
    except Exception as e :
        print('msg.get_msg: ',e)