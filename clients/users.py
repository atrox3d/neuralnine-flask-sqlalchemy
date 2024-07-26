import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--login', nargs=2)
parser.add_argument('-u', '--login-uid')
parser.add_argument('-s', '--signup', nargs=2)
parser.add_argument('-L', '--logout', action='store_true',
                    default=False)

args = parser.parse_args()
print(args)


SERVER = 'http://127.0.0.1:5000'

def signup(username, password):
    payload = dict(username=username, password=password)
    response = requests.post(f'{SERVER}/signup', json=payload)
    response.raise_for_status()
    return response

def login(username, password):
    payload = dict(username=username, password=password)
    response = requests.post(f'{SERVER}/login', json=payload)
    response.raise_for_status()
    return response

def login_uid(uid):
    response = requests.get(f'{SERVER}/login/{uid}')
    response.raise_for_status()
    return response

def logout():
    response = requests.post(f'{SERVER}/logout')
    response.raise_for_status()
    return response

def index():
    response = requests.get(f'{SERVER}/')
    response.raise_for_status()
    return response

def print_response(response):
    print(json.dumps(response.json()))

if args.signup is not None:
    response = signup(*args.signup)
    print_response(response)

elif args.login is not None:
    response = login(*args.login)
    print_response(response)

elif args.logout:
    response = logout()
    print_response(response)

elif args.login_uid:
    response = login_uid(args.login_uid)
    print_response(response)

else:
    response = index()
    print_response(response)
