from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class FlaskApp:
    __initialized: bool = False

    def __init__(self, name:str, dbpath:str='data.db') -> None:
        if self.__initialized:
            raise ValueError(f'FlaskApp is already initialized')
        self.__name = name
        self.__dbpath = dbpath
        self.__app = Flask(self.__name)
        self.__app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{self.__dbpath}'
        self.__db = SQLAlchemy(self.__app)
        FlaskApp.__initialized = True

    def app(self):
        return self.__app

    def db(self):
        return self.__db

