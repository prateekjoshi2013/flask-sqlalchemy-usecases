'''
automap method tries to create orm classes from existing table 
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Purchase = Base.classes.purchase
Customer = Base.classes.customer

'''
db.session.query(Purchase).all()
[<sqlalchemy.ext.automap.purchase object at 0x7f5a2bf78fa0>, <sqlalchemy.ext.automap.purchase object at 0x7f5a2bf78f40>, <sqlalchemy.ext.automap.purchase object at 0x7f5a2bf79000>, <sqlalchemy.ext.automap.purchase object at 0x7f5a2bf79150>, <sqlalchemy.ext.automap.purchase object at 0x7f5a2bf79210>, <sqlalchemy.ext.automap.purchase object at 0x7f5a2bf792d0>, <sqlalchemy.ext.automap.purchase object at 0x7f5a2bf79390>, <sqlalchemy.ext.automap.purchase object at 0x7f5a2bf79450>, <sqlalchemy.ext.automap.purchase object at 0x7f5a2bf79510>, <sqlalchemy.ext.automap.purchase object at 0x7f5a2bf795d0>]
>>> for r in db.session.query(Purchase).all():
...     print(f'id:{r.id} name:{r.price}')

id:1 name:49
id:2 name:56
id:3 name:56
id:4 name:97
id:5 name:20
id:6 name:34
id:7 name:49
id:8 name:20
id:9 name:56
id:10 name:49



---------------------------------------------Adding a new object

>>> db.session.add(Customer(name='Prateek'))
>>> db.session.commit()


-------------------------------------------Inner join

results=db.session.query(Customer.name,Purchase.id,Purchase.price).join(Purchase,Purchase.customer_id==Customer.id).all()
>>> for r in results:
...     print(f'customer_name: {r[0]} purchase_id: {r[1]} price: {r[2]}')
... 
customer_name: John purchase_id: 1 price: 49
customer_name: John purchase_id: 2 price: 56
customer_name: John purchase_id: 3 price: 56
customer_name: John purchase_id: 4 price: 97
customer_name: John purchase_id: 5 price: 20
customer_name: John purchase_id: 6 price: 34
customer_name: John purchase_id: 7 price: 49
customer_name: John purchase_id: 8 price: 20
customer_name: Anthony purchase_id: 9 price: 56
customer_name: Anthony purchase_id: 10 price: 49
customer_name: Anthony purchase_id: 11 price: 97
customer_name: Anthony purchase_id: 12 price: 12
customer_name: Anthony purchase_id: 13 price: 12
customer_name: Anthony purchase_id: 14 price: 56
customer_name: Paul purchase_id: 15 price: 20
customer_name: Paul purchase_id: 16 price: 34
customer_name: Paul purchase_id: 17 price: 56
customer_name: Paul purchase_id: 18 price: 97
customer_name: Paul purchase_id: 19 price: 97
customer_name: Polly purchase_id: 20 price: 12
'''