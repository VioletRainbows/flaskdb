import os

from flask import Flask
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.sql.ddl import CreateSchema, DropSchema

from flaskdb.data_models import User
from flaskdb.database import db

app = Flask(__name__)


@app.route('/')
def new_user():
    db.session.add(User(username='username'))
    db.session.commit()
    return 'New user created!!'


if __name__ == '__main__':
    DATABASE_URI = os.getenv('DATABASE_URI')
    assert DATABASE_URI, 'Environment variable "DATABASE_URI" required.'
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)

    try:
        db.engine.execute(DropSchema('tests', cascade=True))
    except ProgrammingError:
        pass
    db.engine.execute(CreateSchema('tests'))

    db.create_all()

    app.run()
