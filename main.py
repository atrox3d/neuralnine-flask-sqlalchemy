import flask_factory
import models

app = flask_factory.get_app()

app.run(debug=True)
