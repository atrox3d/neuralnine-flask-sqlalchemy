import flask_app as fa

db = fa.get_db(__name__)
print(db)
print(fa.get_app(__name__))