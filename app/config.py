import os
import secrets

class config:
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(16))