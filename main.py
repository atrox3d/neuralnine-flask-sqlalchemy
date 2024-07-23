from flask_migrate import Migrate

import flask_factory
from models import Person
# import routes.application as application
from routes import application, login

app = flask_factory.get_app()
db = flask_factory.get_db()

# with app.app_context():
    # db.drop_all()
    # db.create_all()

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
