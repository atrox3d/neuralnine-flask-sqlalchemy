from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from models.the_db import db
# imports for migration
from models.person import Person
from models.user import User

from routes import application, login, sessions
import the_app

# app = Flask('__name__')
app = the_app.app(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///data.db'
db.init_app(app)

app.secret_key = 'SECRETKEY'
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(uid):
    user = User.query.get(uid)
    return user

bcrypt = Bcrypt(app)

# with app.app_context():
    # db.drop_all()
    # db.create_all()

application.register_routes(app, db)
login.register_routes(app, db, bcrypt)
sessions.register_routes(app, db)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
