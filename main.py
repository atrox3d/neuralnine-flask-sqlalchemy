from flask_app import FlaskApp

fa = FlaskApp(__name__)
# fa = FlaskApp(__name__)
db = fa.get_db()
print(db)
print(fa.get_app())