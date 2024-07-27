import json
import main
import sys

# from app.models import Stock
from models.the_db import db
from models.user import User
from main import setup_app
from main import the_app


def setup_module(module):
    print(f'SETUP_MODULE | setting up MODULE {module}')

def teardown_module(module):
    print(f'TEARDOWN_MODULE | tearing down MODULE {module}')
    print(f'TEARDOWN_MODULE | resetting app')
    the_app.reset()

class TestLogin:

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

    # @classmethod
    # def teardown_class(cls):
    #     del cls.app
    #     del cls.db

    def setup_method(self):
        self.USERNAME = 'testuser'
        self.PASSWORD = '12345'
        self.TEST_RESPONSE = {
            'description': None,
            'password': self.PASSWORD,
            'role': None,
            'uid': 1,
            'username': self.USERNAME
        }
        self.NO_USERS = {'index': 'no user'}

        print(f'SETUP_METOD | resetting test db')
        with self.app.app_context():
            self.db.drop_all()
            self.db.create_all()
    
    def add_user(self):
        print(f'SETUP_METOD | adding user')
        with self.app.app_context():
            db.session.add(
                User(
                    username=self.USERNAME,
                    password=self.PASSWORD,
                )
            )
            db.session.commit()

    def teardown_method(self):
        pass
    
    def test_no_users_logged(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.json == self.NO_USERS

    def test_login_id_1(self):
        with self.client.session_transaction():
            response = self.client.get("/")
            assert response.status_code == 200
            assert response.json == self.NO_USERS

            self.add_user()

            response = self.client.get("/login/1")
            assert response.status_code == 200
            assert response.json == {'login': self.TEST_RESPONSE }

            response = self.client.get("/")
            assert response.status_code == 200
            # assert response.json == self.NO_USERS
            print(response.json)
            assert response.json == {'index': self.TEST_RESPONSE}


    def test_login_id_1_without_session(self):
        # self.client.session_transaction()
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.json == self.NO_USERS

        self.add_user()

        response = self.client.get("/login/1")
        assert response.status_code == 200
        assert response.json == {'login': self.TEST_RESPONSE }

        response = self.client.get("/")
        assert response.status_code == 200
        # assert response.json == self.NO_USERS
        print(response.json)
        assert response.json == {'index': self.TEST_RESPONSE}


    #     assert isinstance(response.json, list)
    #     assert len(response.json) == 0

