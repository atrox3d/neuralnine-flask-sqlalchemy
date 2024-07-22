from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

__app: Flask = None
__db: SQLAlchemy = None

def get_app(name:str=__name__):
    global __app 
    
    if __app is None:
        __app= Flask(name)
    return __app

def get_db(name:str=__name__):
    global __db

    if __db is None:
        app = get_app(name)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        __db = SQLAlchemy(app)
    return __db



