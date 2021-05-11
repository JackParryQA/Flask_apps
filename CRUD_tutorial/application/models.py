from flask.app import Flask
from flask_sqlalchemy.model import Model
from application import db

class Games(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)