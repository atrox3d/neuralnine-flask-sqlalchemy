from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from models.the_db import db
# imports for migration
from models.person import Person
from models.user import User

from routes import application, login, sessions, cookies
import the_app

def init_app(name, **config):
    # app = Flask('__name__')
    app = the_app.app(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///data.db'
    app.config.update(**config)
    return app

def init_db(db, app):
    db.init_app(app)
    return db

# app.secret_key = 'SECRETKEY'

def init_login(app):
    login_manager = LoginManager(app)
    @login_manager.user_loader
    def load_user(uid):
        user = User.query.get(uid)
        return user
    return login_manager

def init_bcrypt(app):
    bcrypt = Bcrypt(app)
    return bcrypt

# with app.app_context():
    # db.drop_all()
    # db.create_all()
def register_routes(app, db, bcrypt):
    application.register_routes(app, db)
    login.register_routes(app, db, bcrypt)
    sessions.register_routes(app, db)
    cookies.register_routes(app, db)

def migration(app, db):
    migrate = Migrate(app, db)
    return migrate

def setup_app(name, db, **config):
    _app = init_app(name, **config)
    _db = init_db(db, _app)
    _login_manager = init_login(_app)
    _bcrypt = init_bcrypt(_app)
    register_routes(_app, _db, _bcrypt)
    _migrate = migration(_app, _db)
    return _app

def default_app():
    app = setup_app(__name__,
                    db, 
                    SQLALCHEMY_DATABASE_URI=f'sqlite:///data.db',
                    SECRET_KEY='SECRETKEY'
                    )
    return app

if __name__ == '__main__':
    app = default_app()
    app.run(debug=True)
