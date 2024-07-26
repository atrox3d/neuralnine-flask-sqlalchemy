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

def setcookies(session, **payload):
    response = session.post(f'{SERVER}/setcookies', json=payload)
    response.raise_for_status()
    return response

def getcookies(session, **cookies):
    response = session.get(f'{SERVER}/getcookies', 
                        #    cookies=cookies
                           )
    response.raise_for_status()
    return response

def print_response(response):
    print(json.dumps(response.json()))
    print(response.cookies)
    print()

with requests.Session() as s:
    payload = {k:v for pair in args.session for k, v in [pair.split('=')]}
    print_response(setcookies(s, **payload))
    print_response(getcookies(s, **payload))

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
