import requests
import json

SERVER = 'http://127.0.0.1:5000'

def list_people():
    response = requests.get(f'{SERVER}/')
    response.raise_for_status()
    print(json.dumps(response.json(), indent=2))

def add_people(name, age, job):
    payload = dict(name=name, age=age, job=job)
    response = requests.post(f'{SERVER}/add', json=payload)
    response.raise_for_status()
    print(json.dumps(response.json()))


add_people('brian', 12, 'cat')
list_people()