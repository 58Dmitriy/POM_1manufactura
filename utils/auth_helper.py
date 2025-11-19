import os
import base64
from dotenv import load_dotenv

load_dotenv()


def get_auth_credentials():
    """Функция для получения логина и пароля из .env"""
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    if not login or not password:
        raise ValueError("LOGIN or PASSWORD not found in .env file")

    return login, password