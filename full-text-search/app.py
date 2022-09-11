from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_whooshalchemy as wa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whooshdb.sqlite3'
# needed to be true for whoosh to detect changes in db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
app.config['WHOOSH_BASE'] = 'whoosh'


db = SQLAlchemy(app)


class Course(db.Model):
    __searchable__ = ['name,description']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(100))


wa.whoosh_index(app, Course)
db.create_all()
# use m-search because whoosh is not supported anymore 
# https://github.com/honmaple/flask-msearch