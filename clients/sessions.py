import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('session', nargs='+')

# parser.add_argument('-l', '--login', nargs=2)
# parser.add_argument('-u', '--login-uid')
# parser.add_argument('-s', '--signup', nargs=2)
# parser.add_argument('-L', '--logout', action='store_true',
                    # default=False)
# 
args = parser.parse_args()
print(args)

SERVER = 'http://127.0.0.1:5000'

def setsession(session, **payload):
    response = session.post(f'{SERVER}/setsession', json=payload)
    response.raise_for_status()
    return response

def getsession(session):
    response = session.get(f'{SERVER}/getsession')
    response.raise_for_status()
    return response

def print_response(response):
    print(json.dumps(response.json()))

with requests.Session() as s:
    payload = {k:v for pair in args.session for k, v in [pair.split('=')]}
    print_response(setsession(s, **payload))
    print_response(getsession(s))

    # if args.signup is not None:
    #     response = signup(s, *args.signup)
    #     print_response(response)

    # elif args.login is not None:
    #     response = login(s, *args.login)
    #     print_response(response)

    # elif args.logout:
    #     response = logout(s)
    #     print_response(response)

    # elif args.login_uid:
    #     response = login_uid(s, args.login_uid)
    #     print_response(response)

    # else:
    #     response = index(s)
    #     print_response(response)
