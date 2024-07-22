from flask import jsonify, request
import flask_factory as ff
from models import Person
from sqlalchemy import exc

app = ff.get_app()
db = ff.get_db()

def get_people_json():
    people = Person.query.all()
    return jsonify([person.dict() for person in people])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.json)
        person = Person(**request.json)
        try:
            db.session.add(person)
            db.session.commit()
            return get_people_json()
        except exc.IntegrityError as ie:
            return jsonify({'error': str(ie)})

    elif request.method == 'GET':
        return get_people_json()

