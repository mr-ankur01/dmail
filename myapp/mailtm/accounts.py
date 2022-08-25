
import requests,json

def create(address: str, password: str):
    try:
        url = 'https://api.mail.tm/accounts'
        body = {
            'address': address,
            'password': password
        }
        headers = {
            'accept': 'application/ld+json',
            'Content-Type': 'application/ld+json',
        }
        response = requests.post(
            url=url, 
            data=json.dumps(body), 
            headers=headers
        )
        req = response.json()
        return req
    except Exception as e:
        print('account.create: ',e)

def delete(id: str, token: str) -> bool:
    url =f'https://api.mail.tm/accounts/{id}'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/ld+json',
    }
    response = requests.delete(url, headers=headers)
    return response.status_code 


