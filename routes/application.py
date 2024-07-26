from flask import Flask, jsonify, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from models.person import Person

def register_routes(app:Flask, db:SQLAlchemy):

    def get_people_json():
        people = Person.query.all()
        return jsonify([person.dict() for person in people])

    @app.get('/people')
    def get_people():
        people = get_people_json()
        # print(len(people.json))
        return people

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
