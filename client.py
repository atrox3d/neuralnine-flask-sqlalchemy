import requests
import json

def list_people():
    response = requests.get('http://127.0.0.1:5000/')
    print(json.dumps(response.json(), indent=2))

list_people()