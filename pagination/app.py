from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

db.create_all()

'''
Flask-SQLAlchemy Pagination more info
https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.Pagination

use the apgination object returned by paginate query to return the current page 

threads= Thread.query.paginate(per_page=5,page={page_num},error_out=True)

'''