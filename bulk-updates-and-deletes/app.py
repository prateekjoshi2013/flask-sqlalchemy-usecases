from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
db=SQLAlchemy(app)

class Data(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    letter=db.Column(db.String(1))

'''
BULK INSERT

    db.create_all()
    for i in range(100):
        data=Data(letter=choice(choices))
        db.session.add(data)

    db.session.commit()

    Data.query.filter_by(letter='a').all()
    >>>[<Data 10>, <Data 17>, <Data 18>, <Data 25>, <Data 27>, <Data 33>, <Data 38>, <Data 44>, <Data 49>, <Data 51>, <Data 65>, <Data 79>, <Data 85>, <Data 90>, <Data 95>]
    Data.query.filter_by(letter='b').all()
    >>>[<Data 21>, <Data 45>, <Data 84>, <Data 86>, <Data 91>]

BULK UPDATE
    
    Data.query.filter_by(letter='a').update({'letter':'b'})
    >>>15
    Data.query.filter_by(letter='b').all()
    >>>[<Data 10>, <Data 17>, <Data 18>, <Data 21>, <Data 25>, <Data 27>, <Data 33>, <Data 38>, <Data 44>, <Data 45>, <Data 49>, <Data 51>, <Data 65>, <Data 79>, <Data 84>, <Data 85>, <Data 86>, <Data 90>, <Data 91>, <Data 95>]
    Data.query.filter_by(letter='a').all()
    >>>[] 

BULK DELETE

    Data.query.filter_by(letter='b').delete()
    >>> 20
    Data.query.filter_by(letter='b').all()
    >>> []
    
'''