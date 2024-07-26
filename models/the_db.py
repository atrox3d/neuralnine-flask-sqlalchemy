from flask_sqlalchemy import SQLAlchemy

#
# this creates ONE singleton db object, imported from all
# the other modules and initialized later with
# db.init_app(app)
#
db = SQLAlchemy()
