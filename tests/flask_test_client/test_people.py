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
    
    def test_get_people(self):
        response = self.client.get("/people")
        assert response.status_code == 200
        assert isinstance(response.json, list)
        assert len(response.json) == 0
        # assert isinstance(response.json[0], dict)
        # assert tuple(response.json[0].keys()) == ('age', 'job', 'name', 'pid')
        # print(response.json)
        # print(self.app.url_map)
        # return

    def test_add_people(self):
        payload = dict(name='test', age=0, job='nojob')
        response = self.client.post('/add', json=payload)
        assert response.status_code == 200
        assert len(response.json) == 1

        person = Person(pid=1, **payload)
        rperson = Person(**response.json[0])
        assert rperson.dict() == person.dict()
        assert repr(rperson) == repr(person)

    def nope(self):
        for rule in self.app.url_map.iter_rules():
            print(rule)
            print(rule.methods)
        return
        response = self.client.get("/stock/all_stocks/")

        assert response.status_code == 200
        stocks_json = response.json
        assert len(stocks_json) == 3


    # def test_get_stock_by_bad_ticker_integration(self):

    #     response = self.client.get(
    #         f"/stock/TSLA/",
    #         content_type="application/json"
    #     )

    #     assert response.status_code == 200
    #     assert response.json == None


    # def test_add_stock_integration(self):

    # with open(self.test_stock ) as f:
    #     stock_data = json.load(f)

    #     data_json = json.dumps(stock_data)


    # def test_get_stock_by_ticker_conversion_integration(self):

    #     response = self.client.get(
    #         f"/stock/conversion/APPL/GBP",
    #         content_type="application/json"
    #     )


    # def test_add_stock_duplicate_rejected(self):

    #     prices = [
    #         {
    #             "date": "2022-01-01",
    #             "value": 201
    #         },
    #         {
    #             "date": "2022-01-02",
    #             "value": 199
    #         },
    #         {
    #             "date": "2022-01-03",
    #             "value": 205
    #         },
    #         {
    #             "date": "2022-01-04",
    #             "value": 205
    #         },
    #         {
    #             "date": "2022-01-05",
    #             "value": 206
    #         }
    #     ]

    #     stock =  Stock("dave","Microsoft","MSFT",prices)
    #     data_json = stock.__dict__
        
    #     data_json = json.dumps(data_json)
    #     response = self.client.post(
    #         "/add-stock/",
    #         data = data_json,
    #         content_type = "application/json"
    #     )
