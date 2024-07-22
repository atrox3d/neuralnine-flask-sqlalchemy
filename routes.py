from flask import jsonify
import flask_factory

app = flask_factory.get_app()

@app.route('/')
def index():
    return jsonify('hello')

