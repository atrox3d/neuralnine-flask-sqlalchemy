from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class FlaskAppAlreadyInitializedException(Exception):
    pass


class FlaskApp:
    __instance: 'FlaskApp' = None

    def __init__(self, name:str=__name__, dbpath:str='data.db') -> None:
        if self.__instance:
            raise FlaskAppAlreadyInitializedException(f'FlaskApp is already initialized')
        self.__name = name
        self.__dbpath = dbpath
        self.__app = Flask(self.__name)
        self.__app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{self.__dbpath}'
        self.__db = SQLAlchemy(self.__app)
        FlaskApp.__instance = self

    @classmethod
    def get_instance(cls, name:str=__name__, dbpath:str='data.db') -> 'FlaskApp':
        try:
            return cls(name, dbpath)
        except FlaskAppAlreadyInitializedException:
            return cls.__instance

    def get_app(self) -> Flask:
        return self.__app

    def get_db(self) -> SQLAlchemy:
        return self.__db
