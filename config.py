from os import environ
from dotenv import load_dotenv

# Load environment variables from `.env`;
load_dotenv()

class DevConfig:
    """Flask configuration for development. Load variables from `.env`;"""
    FLASK_APP = environ.get('FLASK_APP')
    SECRET_KEY = environ.get('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = environ.get('WTF_CSRF_SECRET_KEY')
