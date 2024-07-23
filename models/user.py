import flask_factory
import sqlalchemy as sa         # this is really horrible, there is no intellisense with SQLAlchemy module
from flask_login import UserMixin

db = flask_factory.get_db()

class User(db.Model, UserMixin):

    __tablename__ = 'users'
    
    uid = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.Text, nullable=False)
    password = sa.Column(sa.Text, nullable=False)
    role = sa.Column(sa.String)
    description = sa.Column(sa.String)

    def __repr__(self) -> dict:
        return f'{self.username} ({self.role})'
    
    def dict(self):
        return {
            'uid': self.uid,
            'username': self.username,
            'password': self.password,
            'role': self.role,
            'description': self.description,
        }
