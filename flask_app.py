from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class FlaskApp:
    __name: str = None
    __dbpath: str = None
    __app: Flask = None
    __db: SQLAlchemy = None

    def __init__(self, name:str, dbpath:str='data.db') -> None:
        if FlaskApp.__app is None:
            FlaskApp.__name = name
            FlaskApp.__app = Flask(FlaskApp.__name)
            FlaskApp.__app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{FlaskApp.__dbpath}'
            FlaskApp.__db = SQLAlchemy(FlaskApp.__app)
        else:
            raise ValueError(f'{FlaskApp.__app} is already initialized')

    def get_app(self):
        return FlaskApp.__app

    def get_db(self):
        return FlaskApp.__db

