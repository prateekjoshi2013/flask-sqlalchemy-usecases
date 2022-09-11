'''
reflection methiod does not create orm classes from existing table 
can be queried only
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

customer = db.Table('customer', db.metadata,
                    autoload=True, autoload_with=db.engine)

'''
----------------------------------------------DATABASE QUERY (autoload can only run the session.query) -----------------
>>> db.session.query(customer).all()
[(1, 'John'), (2, 'Anthony'), (3, 'Paul'), (4, 'Polly')]
>>> 
'''
