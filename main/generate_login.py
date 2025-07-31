import random

def generate_numeric_login(length=12):
    return ''.join(random.choices('0123456789', k=length))