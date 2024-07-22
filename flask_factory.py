from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_app import FlaskApp

def get_app(name:str=__name__, dbpath:str='data.db') -> Flask:
    return FlaskApp.get_instance(name, dbpath).get_app()

def get_db() -> SQLAlchemy:
    return FlaskApp.get_instance().get_db()

