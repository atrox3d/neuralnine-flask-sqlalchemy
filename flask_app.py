from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class FlaskAppAlreadyInitializedException(Exception):
    pass

class FlaskApp:
    __instance: 'FlaskApp' = None

    def __init__(self, name:str, dbpath:str='data.db') -> None:
        if self.__instance:
            raise FlaskAppAlreadyInitializedException(f'FlaskApp is already initialized')
        self.__name = name
        self.__dbpath = dbpath
        self.__app = Flask(self.__name)
        self.__app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{self.__dbpath}'
        self.__db = SQLAlchemy(self.__app)
        FlaskApp.__instance = self

    def app(self):
        return self.__app

    def db(self):
        return self.__db

