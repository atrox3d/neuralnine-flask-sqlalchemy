from flask import jsonify, redirect, request, url_for
import flask_factory as ff
from models.person import Person
from sqlalchemy import exc

app = ff.get_app()
db = ff.get_db()

# it is possible to have multiple routes to the same endpoint
# @app.get('/login')
# def login_get():
#     return 'login_get'

# # this is ignored
# @app.get('/login')
# def login_get2():
#     return 'login_get2'

@app.post('/signup')
def signup():
    return 'signup'

@app.post('/login')
def login():
    return 'login'

@app.post('/logout')
def logout():
    return 'login'
