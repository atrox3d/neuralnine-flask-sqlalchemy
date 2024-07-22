import flask_factory
from models import Person
import routes

app = flask_factory.get_app()
db = flask_factory.get_db()

with app.app_context():
    db.drop_all()
    db.create_all()


app.run(debug=True)
