import json
import main

# from app.models import Stock
from models.the_db import db
from models.person import Person
from main import setup_app

class TestPeople:

    @classmethod
    def setup_class(cls):
        cls.db = db
        print(f'SETUP_CLASS | setting up app')
        cls.app = setup_app(__name__,
                            cls.db,
                            SQLALCHEMY_DATABASE_URI=f'sqlite:///test_data.db',
                            SECRET_KEY='SECRETKEY'
                             )

        # print(self.app.config)
        print(f'SETUP_CLASS | setting up test client')
        with cls.app.test_client() as client:
            cls.client = client

    def setup_method(self):
        print(f'SETUP_METOD | resetting test db')
        with self.app.app_context():
            self.db.drop_all()
            self.db.create_all()

    def teardown_method(self):
        pass

    def add_people(self, name, age, job):
        payload = dict(name=name, age=age, job=job)
        response = self.client.post('/add', json=payload)
        return response

    def delete_people(self, pid):
        payload = dict(pid=pid)
        response = self.client.delete('/delete', json=payload)
        return response
        
    def test_get_people(self):
        response = self.client.get("/people")
        assert response.status_code == 200
        assert isinstance(response.json, list)
        assert len(response.json) == 0

    def test_add_people(self):
        payload = dict(name='test', age=0, job='nojob')
        response = self.add_people(**payload)
        assert response.status_code == 200
        assert len(response.json) == 1

        person = Person(pid=1, **payload)
        rperson = Person(**response.json[0])
        assert rperson.dict() == person.dict()
        assert repr(rperson) == repr(person)

        response = self.client.get("/people")
        assert response.status_code == 200
        assert len(response.json) == 1

    def test_delete_people(self):
        payload = dict(name='test', age=0, job='nojob')
        response = self.add_people(**payload)
        assert response.status_code == 200

        response = self.client.get("/people")
        assert response.status_code == 200
        assert len(response.json) == 1

        response = self.delete_people(1)
        assert response.status_code == 200
        assert len(response.json) == 0

    def nope(self):
        for rule in self.app.url_map.iter_rules():
            print(rule)
            print(rule.methods)
        return
        response = self.client.get("/stock/all_stocks/")

        assert response.status_code == 200
        stocks_json = response.json
        assert len(stocks_json) == 3


