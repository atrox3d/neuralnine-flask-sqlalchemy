from flask import Flask, jsonify, redirect, request, session, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from models.person import Person

def register_routes(app:Flask, db:SQLAlchemy):

    @app.post('/setcookies')
    def setcookies():
        response = make_response({})
        print(f'setcookies: {response = }')
        for k, v in request.json.items():
            response.set_cookie(k, v)
        print(f'setcookies: {response = }')
        return response

    @app.get('/getcookies')
    def getcookies():
        print(f'getcookies: {request.cookies = }')
        response = make_response(request.cookies)
        for k,  v in request.cookies.items():
            response.set_cookie(k, v)
        return response

