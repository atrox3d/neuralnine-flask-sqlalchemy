from flask_app import FlaskApp

fa = FlaskApp(__name__)
# fa = FlaskApp(__name__)
db = fa.db()
print(db)
print(fa.app())