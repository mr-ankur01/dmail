import random
import string
from .import domains
BASE_URL = 'https://api.mail.tm'

domain=domains.get()

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