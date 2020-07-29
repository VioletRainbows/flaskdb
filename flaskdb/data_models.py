from sqlalchemy import Column, String

from flaskdb.database import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'tests'}

    username = Column(String(64), primary_key=True)
