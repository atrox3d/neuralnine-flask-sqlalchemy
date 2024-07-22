from flask import jsonify
import flask_factory
from models import Person

app = flask_factory.get_app()

@app.route('/')
def index():
    people = Person.query.all()
    return jsonify(people)

