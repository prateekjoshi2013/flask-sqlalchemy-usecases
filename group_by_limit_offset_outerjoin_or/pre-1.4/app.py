from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True

db=SQLAlchemy(app)

class Customer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    orders=db.relationship('Purchase',backref='customer')

class Purchase(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    customer_id=db.Column(db.Integer,db.ForeignKey('customer.id'))
    price=db.Column(db.Integer)

'''
--------------------------------------------------------OR QUERY-----------------------------------------------------

>>> results=Customer.query.filter(db.or_(Customer.name=='Anthony',Customer.name=='Polly')).all()
2022-09-13 20:35:01,175 INFO sqlalchemy.engine.Engine SELECT customer.id AS customer_id, customer.name AS customer_name 
FROM customer 
WHERE customer.name = ? OR customer.name = ?
2022-09-13 20:35:01,175 INFO sqlalchemy.engine.Engine [generated in 0.00027s] ('Anthony', 'Polly')
>>> print(results)
[<Customer 2>, <Customer 4>]
--------------------------------------------------------------LEFT OUTER JOIN--------------------------------------------------------

>>> db.session.query(Customer,Purchase).outerjoin(Purchase,Purchase.customer_id==Customer.id).all()
 BEGIN (implicit)
 SELECT customer.id AS customer_id, customer.name AS customer_name, purchase.id AS purchase_id, purchase.customer_id AS purchase_customer_id, purchase.price AS purchase_price 
 FROM customer LEFT OUTER JOIN purchase ON purchase.customer_id = customer.id
 [generated in 0.00027s] ()
 [(<Customer 1>, <Purchase 5>), 
 (<Customer 1>, <Purchase 8>), 
 (<Customer 1>, <Purchase 6>), 
 (<Customer 1>, <Purchase 1>), 
 (<Customer 1>, <Purchase 7>), 
 (<Customer 1>, <Purchase 2>), 
 (<Customer 1>, <Purchase 3>), 
 (<Customer 1>, <Purchase 4>), 
 (<Customer 2>, <Purchase 12>), 
 (<Customer 2>, <Purchase 13>), 
 (<Customer 2>, <Purchase 10>), 
 (<Customer 2>, <Purchase 9>), 
 (<Customer 2>, <Purchase 14>), 
 (<Customer 2>, <Purchase 11>), 
 (<Customer 3>, <Purchase 15>), 
 (<Customer 3>, <Purchase 16>), 
 (<Customer 3>, <Purchase 17>), 
 (<Customer 3>, <Purchase 18>), 
 (<Customer 3>, <Purchase 19>), 
 (<Customer 4>, <Purchase 20>)]
>>> results=db.session.query(Customer,Purchase).outerjoin(Purchase,Purchase.customer_id==Customer.id).all()
>>> for r in results:
...     print(f'id: {r[0].id} name: {r[0].name} order_id: {r[1].id} price: {r[1].price}')
... 
id: 1 name: John order_id: 5 price: 20
id: 1 name: John order_id: 8 price: 20
id: 1 name: John order_id: 6 price: 34
id: 1 name: John order_id: 1 price: 49
id: 1 name: John order_id: 7 price: 49
id: 1 name: John order_id: 2 price: 56
id: 1 name: John order_id: 3 price: 56
id: 1 name: John order_id: 4 price: 97
id: 2 name: Anthony order_id: 12 price: 12
id: 2 name: Anthony order_id: 13 price: 12
id: 2 name: Anthony order_id: 10 price: 49
id: 2 name: Anthony order_id: 9 price: 56
id: 2 name: Anthony order_id: 14 price: 56
id: 2 name: Anthony order_id: 11 price: 97
id: 3 name: Paul order_id: 15 price: 20
id: 3 name: Paul order_id: 16 price: 34
id: 3 name: Paul order_id: 17 price: 56
id: 3 name: Paul order_id: 18 price: 97
id: 3 name: Paul order_id: 19 price: 97
id: 4 name: Polly order_id: 20 price: 12

>>> results=db.session.query(Customer.id,Customer.name,Purchase.id,Purchase.price).outerjoin(Purchase,Purchase.customer_id==Customer.id).all()
2022-09-13 19:45:11,381 INFO sqlalchemy.engine.Engine SELECT customer.id AS customer_id, customer.name AS customer_name, purchase.id AS purchase_id, purchase.price AS purchase_price 
FROM customer LEFT OUTER JOIN purchase ON purchase.customer_id = customer.id
2022-09-13 19:45:11,381 INFO sqlalchemy.engine.Engine [generated in 0.00058s] ()
>>> for r in results:
...     print(f'id: {r[0]} name: {r[1]} order_id: {r[2]} price: {r[3]}')
... 
id: 1 name: John order_id: 5 price: 20
id: 1 name: John order_id: 8 price: 20
id: 1 name: John order_id: 6 price: 34
id: 1 name: John order_id: 1 price: 49
id: 1 name: John order_id: 7 price: 49
id: 1 name: John order_id: 2 price: 56
id: 1 name: John order_id: 3 price: 56
id: 1 name: John order_id: 4 price: 97
id: 2 name: Anthony order_id: 12 price: 12
id: 2 name: Anthony order_id: 13 price: 12
id: 2 name: Anthony order_id: 10 price: 49
id: 2 name: Anthony order_id: 9 price: 56
id: 2 name: Anthony order_id: 14 price: 56
id: 2 name: Anthony order_id: 11 price: 97
id: 3 name: Paul order_id: 15 price: 20
id: 3 name: Paul order_id: 16 price: 34
id: 3 name: Paul order_id: 17 price: 56
id: 3 name: Paul order_id: 18 price: 97
id: 3 name: Paul order_id: 19 price: 97
id: 4 name: Polly order_id: 20 price: 12

--------------------------------------------------------GROUP BY QUERY-----------------------------------------------------

>>> results=db.session.query(Customer.name,db.func.count(Purchase.customer_id)).outerjoin(Purchase,Customer.id==Purchase.customer_id).group_by(Customer.name).all()
2022-09-13 20:00:37,417 INFO sqlalchemy.engine.Engine SELECT customer.name AS customer_name, count(purchase.customer_id) AS count_1 
FROM customer LEFT OUTER JOIN purchase ON customer.id = purchase.customer_id GROUP BY customer.name
2022-09-13 20:00:37,417 INFO sqlalchemy.engine.Engine [generated in 0.00021s] ()
>>> print(results)
[('Anthony', 6), ('John', 8), ('Paul', 5), ('Polly', 1)]
>>> 

>>> results=db.session.query(Customer.name,db.func.sum(Purchase.price)).outerjoin(Purchase,Customer.id==Purchase.customer_id).group_by(Customer.name).all()
2022-09-13 20:02:26,652 INFO sqlalchemy.engine.Engine SELECT customer.name AS customer_name, sum(purchase.price) AS sum_1 
FROM customer LEFT OUTER JOIN purchase ON customer.id = purchase.customer_id GROUP BY customer.name
2022-09-13 20:02:26,652 INFO sqlalchemy.engine.Engine [generated in 0.00036s] ()
>>> print(results)
[('Anthony', 282), ('John', 381), ('Paul', 304), ('Polly', 12)]
>>> 

--------------------------------------------------------ORDER BY QUERY-----------------------------------------------------

>>> results=db.session.query(Customer.name,db.func.sum(Purchase.price)).outerjoin(Purchase,Customer.id==Purchase.customer_id).group_by(Customer.name).order_by(Customer.name).all()
2022-09-13 20:25:32,049 INFO sqlalchemy.engine.Engine SELECT customer.name AS customer_name, sum(purchase.price) AS sum_1 
FROM customer LEFT OUTER JOIN purchase ON customer.id = purchase.customer_id GROUP BY customer.name ORDER BY customer.name
2022-09-13 20:25:32,050 INFO sqlalchemy.engine.Engine [generated in 0.00056s] ()
>>> print(results)
[('Anthony', 282), ('John', 381), ('Paul', 304), ('Polly', 12)]
>>>

>>> results=db.session.query(Customer.name,db.func.sum(Purchase.price)).outerjoin(Purchase,Customer.id==Purchase.customer_id).group_by(Customer.name).order_by(db.func.sum(Purchase.price).desc()).all()
2022-09-13 20:28:55,314 INFO sqlalchemy.engine.Engine SELECT customer.name AS customer_name, sum(purchase.price) AS sum_1 
FROM customer LEFT OUTER JOIN purchase ON customer.id = purchase.customer_id GROUP BY customer.name ORDER BY sum(purchase.price) DESC
2022-09-13 20:28:55,314 INFO sqlalchemy.engine.Engine [generated in 0.00021s] ()
>>> print(results)
[('John', 381), ('Paul', 304), ('Anthony', 282), ('Polly', 12)]
>>> 
--------------------------------------------------------ORDER BY QUERY-----------------------------------------------------

>>> result=Customer.query.order_by(Customer.name.desc()).all()
2022-09-13 20:31:03,054 INFO sqlalchemy.engine.Engine SELECT customer.id AS customer_id, customer.name AS customer_name 
FROM customer ORDER BY customer.name DESC
2022-09-13 20:31:03,054 INFO sqlalchemy.engine.Engine [generated in 0.00058s] ()
>>> print(results)
[('John', 381), ('Paul', 304), ('Anthony', 282), ('Polly', 12)]
>>> 


--------------------------------------------------------OFFSET QUERY-----------------------------------------------------

>>> Purchase.query.limit(10).all()
2022-09-13 20:39:46,204 INFO sqlalchemy.engine.Engine SELECT purchase.id AS purchase_id, purchase.customer_id AS purchase_customer_id, purchase.price AS purchase_price 
FROM purchase
 LIMIT ? OFFSET ?
2022-09-13 20:39:46,204 INFO sqlalchemy.engine.Engine [generated in 0.00024s] (10, 0)
[<Purchase 1>, <Purchase 2>, <Purchase 3>, <Purchase 4>, <Purchase 5>, <Purchase 6>, <Purchase 7>, <Purchase 8>, <Purchase 9>, <Purchase 10>]

--------------------------------------------------------LIMIT & OFFSET QUERY-----------------------------------------------------

>>> Purchase.query.limit(10).offset(5).all()
2022-09-13 20:41:44,453 INFO sqlalchemy.engine.Engine SELECT purchase.id AS purchase_id, purchase.customer_id AS purchase_customer_id, purchase.price AS purchase_price 
FROM purchase
 LIMIT ? OFFSET ?
2022-09-13 20:41:44,453 INFO sqlalchemy.engine.Engine [generated in 0.00069s] (10, 5)
[<Purchase 6>, <Purchase 7>, <Purchase 8>, <Purchase 9>, <Purchase 10>, <Purchase 11>, <Purchase 12>, <Purchase 13>, <Purchase 14>, <Purchase 15>]
>>> 

'''