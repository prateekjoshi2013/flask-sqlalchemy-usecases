from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    child = db.relationship('Child', backref='parent', uselist=False)


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), unique=True)


# db.create_all()
'''
    for more info in relationship patterns supported by SQLAlchemy 
    https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
'''