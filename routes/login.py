import bcrypt
from flask import Flask, jsonify, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user, current_user, login_required

from models.user import User

def register_routes(app:Flask, db:SQLAlchemy, bcrypt:Bcrypt):

    @app.get('/')
    def index():
        if current_user.is_authenticated:
            return current_user.dict()
        else:
            return {'index': 'no user'}

    @app.get('/login/<uid>')
    def login(uid):
        user:User = User.query.get(uid)
        login_user(user)
        return {'login': user.dict()}

    @app.get('/logout')
    def logout():
        logout_user()
        return {'logout': 'Success'}

    @app.post('/signup')
    def signup():
        return {'signup': True}

    # it is possible to have multiple routes to the same endpoint
    # @app.get('/login')
    # def login_get():
    #     return 'login_get'

    # # this is ignored
    # @app.get('/login')
    # def login_get2():
    #     return 'login_get2'
