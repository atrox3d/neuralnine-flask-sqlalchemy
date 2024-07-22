import flask_factory
import sqlalchemy as sa         # this is really horrible, there is no intellisense with SQLAlchemy module

db = flask_factory.get_db()

class Person(db.Model):

    __tablename__ = 'people'
    
    pid = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False)
    age = sa.Column(sa.Integer)
    job = sa.Column(sa.Text)

    def __repr__(self) -> dict:
        return f'{self.name} ({self.age}): {self.job}'
    
    def dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'job': self.job
        }
