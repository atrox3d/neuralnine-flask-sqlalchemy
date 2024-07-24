from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

import flask_factory
# import routes.application as application
from routes import application, login

app = flask_factory.get_app()
db = flask_factory.get_db()

app.secret_key = 'SECRETKEY'
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)

# bcrypt =

# with app.app_context():
    # db.drop_all()
    # db.create_all()

# imports for migration
from models.person import Person
from models.user import User
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
