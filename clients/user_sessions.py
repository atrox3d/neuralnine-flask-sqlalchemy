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

def signup(session, username, password):
    payload = dict(username=username, password=password)
    response = session.post(f'{SERVER}/signup', json=payload)
    response.raise_for_status()
    return response

def login(session, username, password):
    payload = dict(username=username, password=password)
    response = session.post(f'{SERVER}/login', json=payload)
    response.raise_for_status()
    return response

def login_uid(session, uid):

    # def print_session(session):
        # print(vars(session))
        # print()
# 
    # def print_response(response):
        # print(vars(response))
        # print(f'{response         = }')
        # print(f'{response.json()  = }')
        # print(f'{response.cookies = }')
        # print(f'{response.headers = }')
        # print()

    # with requests.Session() as s:

    response = session.get(f'{SERVER}/login/{uid}')
        # r = s.get('https://httpbin.org/cookies')
        # print_response(response)
        # print_session(s)
        # 
        # response = s.get(f'{SERVER}/')
        # print_response(response)
        # print_session(s)
# 
        # response = s.get(f'{SERVER}/')
        # print_response(response)
        # print_session(s)
# 
        # exit()
        # '{"cookies": {"sessioncookie": "123456789"}}'

    return response
    response = requests.get(f'{SERVER}/login/{uid}')
    response.raise_for_status()
    return response

def logout(session):
    response = session.get(f'{SERVER}/logout')
    response.raise_for_status()
    return response

def index(session):
    response = session.get(f'{SERVER}/')
    response.raise_for_status()
    return response

def print_response(response):
    print(json.dumps(response.json()))

with requests.Session() as s:
    print_response(login_uid(s, 1))
    print_response(index(s))
    print_response(index(s))
    print_response(logout(s))
    print_response(index(s))
    exit()


    if args.signup is not None:
        response = signup(s, *args.signup)
        print_response(response)

    elif args.login is not None:
        response = login(s, *args.login)
        print_response(response)

    elif args.logout:
        response = logout(s)
        print_response(response)

    elif args.login_uid:
        response = login_uid(s, args.login_uid)
        print_response(response)

    else:
        response = index(s)
        print_response(response)
