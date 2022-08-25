import random
import string




BASE_URL = 'https://api.mail.tm'
domain ='@arxxwalls.com'


def generate_password():
    CHARS = string.ascii_letters + string.digits
    chatset = [random.choice(CHARS) for _ in range(10)]
    return ''.join(chatset)

def generate_address():
    CHARS = string.ascii_lowercase + string.digits
    chatset = [random.choice(CHARS) for _ in range(10)]
    return ''.join(chatset)

address = generate_address() + domain
password = generate_password() 