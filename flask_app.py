from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class FlaskAppAlreadyInitializedException(Exception):
    pass


class FlaskApp:
    __instance: 'FlaskApp' = None

    def __init__(self, name:str=__name__, dbpath:str='data.db') -> None:
        if self.__instance:
            raise FlaskAppAlreadyInitializedException(f'FlaskApp is already initialized')
        self.name = name
        self.dbpath = dbpath
        self.app = Flask(self.name)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{self.dbpath}'
        self.db = SQLAlchemy(self.app)
        FlaskApp.__instance = self

    @classmethod
    def get_instance(cls, name:str=__name__, dbpath:str='data.db') -> 'FlaskApp':
        try:
            return cls(name, dbpath)
        except FlaskAppAlreadyInitializedException:
            return cls.__instance

    def get_app(self) -> Flask:
        return self.app

    def get_db(self) -> SQLAlchemy:
        return self.db
