import json
import main

# from app.models import Stock


class TestClass:

    # db_path = 'project/Hands-on-Test-Driven-Development-TDD-using-Python/db/stock_db.json'
    # test_stock = 'project/Hands-on-Test-Driven-Development-TDD-using-Python/db/stock_db.json'
    # db_path = 'db/stock_db.json'

    @classmethod
    def setup_method(self):
        self.app = main.app
        self.app.config["TESTING"] = True

        with self.app.test_client() as client:
            self.client = client

    @classmethod
    def teardown_method(self):
        # original_stocks = self.return_original_stocks(self)
# 
        # with open(self.db_path,'w') as json_file:
            # json.dump(original_stocks,json_file,indent=4,separators= (',',': '))
        pass
    
    def test_get_all_stocks(self):
        response = self.client.get("/")
        print(response.json)
        print(self.app.url_map)
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
