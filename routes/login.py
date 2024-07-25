from flask import Flask, jsonify, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
import flask_factory as ff
from models.person import Person
from sqlalchemy import exc

def register_routes(app:Flask, db:SQLAlchemy):
    @app.post('/signup')
    def signup():
        return {'signup': True}

    @app.post('/login')
    def login():
        return {'login': True}

    @app.post('/logout')
    def logout():
        return {'logout': True}

    # it is possible to have multiple routes to the same endpoint
    # @app.get('/login')
    # def login_get():
    #     return 'login_get'

    # # this is ignored
    # @app.get('/login')
    # def login_get2():
    #     return 'login_get2'
