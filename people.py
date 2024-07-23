import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', nargs=3)
parser.add_argument('-d', '--delete')
parser.add_argument('-p', '--print', action='store_true',
                    default=False)

args = parser.parse_args()
print(args)


SERVER = 'http://127.0.0.1:5000'

def get_people():
    response = requests.get(f'{SERVER}/')
    response.raise_for_status()
    return response.json()

def print_people(people):
    print(json.dumps(people, indent=2))

def add_people(name, age, job):
    payload = dict(name=name, age=age, job=job)
    response = requests.post(f'{SERVER}/add', json=payload)
    response.raise_for_status()
    print_people(response.json())

def delete_people(id):
    payload = dict(pid=id)
    response = requests.delete(f'{SERVER}/delete', json=payload)
    response.raise_for_status()
    print_people(response.json())

if args.delete is not None:
    delete_people(args.delete)

if args.add is not None:
    add_people(*args.add)

if args.print or args.add is None:
    print_people(get_people())

