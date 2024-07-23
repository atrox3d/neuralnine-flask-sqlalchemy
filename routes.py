from flask import jsonify, redirect, request, url_for
import flask_factory as ff
from models import Person
from sqlalchemy import exc

app = ff.get_app()
db = ff.get_db()

def get_people_json():
    people = Person.query.all()
    return jsonify([person.dict() for person in people])

@app.get('/')
def index():
    return get_people_json()

@app.post('/add')
def add():
    print(f'{request.json = }')
    person = Person(**request.json)
    try:
        print(f'adding {person}')
        db.session.add(person)
        db.session.commit()
        return get_people_json()
    except exc.IntegrityError as ie:
        return jsonify({'error': str(ie)})

@app.delete('/delete')
def delete():
    print(request.json)
    person:Person = Person.query.get(request.json['pid'])
    if person:
        db.session.delete(person)
        db.session.commit()
        return get_people_json()
    else:
        return jsonify({'error': f'cannot find {request.json["pid"]}'})
    