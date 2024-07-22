from flask_app import FlaskApp, FlaskAppAlreadyInitializedException

fa = FlaskApp(__name__)
try:
    fa = FlaskApp(__name__)
except FlaskAppAlreadyInitializedException as faaie:
    print(faaie)
db = fa.db()
print(db)
print(fa.app())