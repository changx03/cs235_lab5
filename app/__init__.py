from flask import Flask
from flask_wtf.csrf import CSRFProtect


def create_app():
    app = Flask(__name__)

    # Apply the CSRFProtect extension
    csrf = CSRFProtect()
    csrf.init_app(app)

    # Load configuration from `config.py`
    app.config.from_object('config.DevConfig')

    return app
