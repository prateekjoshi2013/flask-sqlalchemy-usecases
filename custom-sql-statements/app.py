from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(100))
    pets = db.relationship('Pet', backref='owner')

    def __repr__(self) -> str:
        return f'< Owner id: {self.id} name: {self.name} address: {self.address}'

db.create_all()
'''
    Custom sql query
'''
# db.engine.execute('select count(*) from owner').all()
# [(0,)]
# db.engine.execute("insert into owner values (1,'Prateek','123 sunny lane'),(2,'Mital','234 winter lane')")
# r=db.engine.execute("select * from owner") 
# results=[f'id:{row[0]} name:{row[1]} address:{row[2]}' for row in r  ]
# print(results)
# ['id:1 name:Prateek address:123 sunny lane', 'id:2 name:Mital address:234 winter lane']