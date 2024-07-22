import sys
import json

def validate(item:str):
    parts = item.split('=')
    if len(parts) != 2:
        return False

    name, val = parts
    if not name.isidentifier():
        return False
    
    return True

def get_item(item:str):
    if validate(item):
        name, val = item.split('=')
        return {name:val}
    return None

def jsonify(*args):
    return json.dumps({k:v  for arg in args if validate(arg) for k, v in get_item(arg).items()})

print(jsonify(*sys.argv[1:]))


