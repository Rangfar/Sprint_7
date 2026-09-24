import random
import string
import requests

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_random_phone():
    phone_number = f'+7{random.randint(1000000000, 9999999999)}'
    return phone_number

#относится к дополнительному заданию
def generate_random_number(start, finish):
    random_number = random.randint(start, finish)
    return random_number
