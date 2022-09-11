from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db1.sqlite3'
app.config['SQLALCHEMY_BINDS'] = {'two': 'sqlite:///db2.sqlite3',
                                   'three': 'sqlite:///db3.sqlite3'}
db = SQLAlchemy(app)


class One(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Two(db.Model):
    __bind_key__ = 'two'
    id = db.Column(db.Integer, primary_key=True)


class Three(db.Model):
    __bind_key__ = 'three'
    id = db.Column(db.Integer, primary_key=True)

# for only creating table for a certain bind/binds
# use: 
# db.create_all(bind=['two','three'])
# db.create_all()