from flask import Flask, jsonify, redirect, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from models.person import Person

def register_routes(app:Flask, db:SQLAlchemy):

    @app.post('/setsession')
    def setsession():
        print(f'setsession: {session=}')
        session.update(request.json)
        print(f'setsession: {session=}')
        return {'setsession': session}

    @app.get('/getsession')
    def getsession():
        print(f'getsession: {session=}')
        return {'setsession': session}

