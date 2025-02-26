import os
import secrets


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(16))
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development") # default to development

    if ENVIRONMENT == "production":
        BASE_URL = "https://build-graph-with-tdd-bc2becbeccff.herokuapp.com"
        DEBUG = False

    else:
        BASE_URL = "http://127.0.0.1:5001"
        DEBUG = True