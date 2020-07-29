import os

import pytest
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.sql.ddl import CreateSchema, DropSchema

from flaskdb.app import app as main_app
from flaskdb.database import db


DATABASE_URI = os.getenv('DATABASE_URI')
assert DATABASE_URI, 'Environment variable "DATABASE_URI" required.'


@pytest.fixture(scope='session')
def app():
    main_app.debug = True
    main_app.testing = True

    main_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    main_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return main_app


@pytest.fixture(scope='session')
def database(app, request):
    db.app = app
    db.init_app(app)

    db.drop_all()

    try:
        db.engine.execute(DropSchema('tests', cascade=True))
    except ProgrammingError:
        pass
    db.engine.execute(CreateSchema('tests'))

    db.create_all()

    @request.addfinalizer
    def drop_database():
        db.drop_all()
        db.engine.execute(DropSchema('tests', cascade=True))

    return db


@pytest.fixture(scope='session')
def _db(database):
    return database
