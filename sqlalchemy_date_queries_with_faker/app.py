from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from datetime import date,datetime,timedelta
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date_posted = db.Column(db.Date)
    datetime_posted = db.Column(db.DateTime)

fake = Faker()
'''
db.create_all()


for _ in range(10000):
    transaction_date = fake.date_time_between(start_date='-3y')
    db.session.add(
        Transactions(
            amount=fake.random_int(),
            date_posted=transaction_date.date(),
            datetime_posted=transaction_date
        )
    )

db.session.commit()


transactions=Transactions.query.filter_by(date_posted=date(2022,5,20)).all()

transactions=Transactions.query.filter(func.date(Transactions.datetime_posted)==date(2022,5,20)).all()

transactions=Transactions.query.filter(func.date(Transactions.datetime_posted).between(date(2019,5,20),date(2019,5,20)).all()

# last_date is exlusive
transactions=Transactions.query.filter(func.date(Transactions.datetime_posted).between(date(2019,5,20),date(2022,6,20))).all()

transactions=Transactions.query.filter(Transactions.datetime_posted > date.today()-timedelta(weeks=1)).all()

transactions=Transactions.query.filter(Transactions.datetime_posted > datetime.now()-timedelta(days=30)).all()

transactions=db.session.query(Transactions.date_posted,func.sum(Transactions.amount)).group_by(Transactions.date_posted).order_by(Transactions.date_posted).asc().all()

transactions=db.session.query(Transactions.date_posted,func.sum(Transactions.amount)).group_by(Transactions.date_posted).order_by(Transactions.date_posted.desc()).limit(10).all()

transactions=db.session.query(func.strftime('%Y',Transactions.date_posted),func.sum(Transactions.amount)).group_by(func.strftime('%Y',Transactions.date_posted)).order_by(Transactions.date_posted.asc()).limit(10).all()

transactions=db.session.query(func.strftime('%Y-%m',Transactions.date_posted),func.sum(Transactions.amount)).group_by(func.strftime('%Y-%m',Transactions.date_posted)).order_by(Transactions.date_posted.asc()).limit(10).all()

'''