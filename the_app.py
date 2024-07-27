from flask import Flask

__app: Flask = None

def app(name:str=None, *args, **kwargs) -> Flask:
    global __app
    if name is None:
        if __app is not None:
            return __app
        else:
            raise ValueError('app not initialized')
    else:
        if __app is None:
            __app = Flask(name, *args, **kwargs)
            return __app
        else:
            raise ValueError('app already initialized')

def reset():
    global __app
    __app = None

if __name__ == '__main__':

    try:
        a = app()
        print(f'{a = }')
    except ValueError as ve:
        print(ve)

    try:
        a = app(__name__)
        print(f'{a = }')
    except ValueError as ve:
        print(ve)

    try:
        a = app()
        print(f'{a = }')
    except ValueError as ve:
        print(ve)

    try:
        a = app('new_name')
        print(f'{a = }')
    except ValueError as ve:
        print(ve)

