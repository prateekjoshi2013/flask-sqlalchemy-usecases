from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_BINDS'] = {'two': 'postgresql://kenrbogn:s7pyZ-IYU2MgZutBJzTcXOrQHULh6HTP@jelani.db.elephantsql.com/kenrbogn'}
db = SQLAlchemy(app)


class TableOneInSqlite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(30))
    date= db.Column(db.Date,server_default=db.func.date('now'))

class TableTwoInPostgres(db.Model):
    __bind_key__ = 'two'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(30))
    date= db.Column(db.Date,server_default=db.func.now())
    # time_updated = Column(DateTime(timezone=True), onupdate=func.now())

'''
>>> db.create_all()
>>> for i in range(10):
...     db.session.add(TableOneInSqlite(description=''.join(choices(letters,k=10))))
...     db.session.add(TableTwoInPostgres(description=''.join(choices(letters,k=10))))
...
>>> db.session.commit()

--------------------------------------------SQLITE QUERY-----------------------------------------------
>>> db.session.query(db.func.strftime('%d',TableOneInSqlite.date)).limit(1).scalar()
'14'

--------------------------------------------POSTGRES QUERY-----------------------------------------------
>>> db.session.query(db.func.extract('dow',TableTwoInPostgres.date)).limit(1).scalar()
3.0
>>> db.session.query(db.func.extract('day',TableTwoInPostgres.date)).limit(1).scalar()
14.0
'''