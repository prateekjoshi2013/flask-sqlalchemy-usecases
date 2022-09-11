from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner', lazy='selectin')


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))

'''
-------------------------------------------------------select------------------------------------------------------------------

>>> p=Person.query.filter_by(name='Prateek').first()
BEGIN (implicit)
SELECT person.id AS person_id, person.name AS person_name 
FROM person 
WHERE person.name = ?
 LIMIT ? OFFSET ?
('Prateek', 1, 0) ---time 0.00019s
>>> p.pets
SELECT pet.id AS pet_id, pet.name AS pet_name, pet.owner_id AS pet_owner_id 
FROM pet 
WHERE ? = pet.owner_id
[<Pet 1>, <Pet 2>] ---time 0.00020s
>>> 

-------------------------------------------------------joined------------------------------------------------------------------

>>> p=Person.query.filter_by(name='Prateek').first()
BEGIN (implicit)
SELECT anon_1.person_id AS anon_1_person_id, anon_1.person_name AS anon_1_person_name, pet_1.id AS pet_1_id, pet_1.name AS pet_1_name, pet_1.owner_id AS pet_1_owner_id 
FROM (SELECT person.id AS person_id, person.name AS person_name 
FROM person 
WHERE person.name = ?
 LIMIT ? OFFSET ?) AS anon_1 LEFT OUTER JOIN pet AS pet_1 ON anon_1.person_id = pet_1.owner_id
('Prateek', 1, 0)  ---time 0.00019s
>>> 

-------------------------------------------------------subquery------------------------------------------------------------------


>>> p=Person.query.filter_by(name='Prateek').first()
BEGIN (implicit)
SELECT person.id AS person_id, person.name AS person_name 
FROM person 
WHERE person.name = ?
 LIMIT ? OFFSET ?
('Prateek', 1, 0)  --- time - 0.00020s
SELECT pet.id AS pet_id, pet.name AS pet_name, pet.owner_id AS pet_owner_id, anon_1.person_id AS anon_1_person_id 
FROM (SELECT person.id AS person_id 
FROM person 
WHERE person.name = ?
 LIMIT ? OFFSET ?) AS anon_1 JOIN pet ON anon_1.person_id = pet.owner_id
('Prateek', 1, 0)  --- time - 0.00029s

-------------------------------------------------------selectin------------------------------------------------------------------

>>> p=Person.query.filter_by(name='Prateek').first()
BEGIN (implicit)
SELECT person.id AS person_id, person.name AS person_name 
FROM person 
WHERE person.name = ?
 LIMIT ? OFFSET ?
[generated in 0.00018s] ('Prateek', 1, 0)
SELECT pet.owner_id AS pet_owner_id, pet.id AS pet_id, pet.name AS pet_name 
FROM pet 
WHERE pet.owner_id IN (?)
[generated in 0.00044s] (1,)

'''


'''
LOADING RELATIONSHIPS

https://docs.sqlalchemy.org/en/14/orm/loading_relationships.html

options for lazy parameters:

LAZY LOADING - 

available via lazy='select' or the lazyload() option, 
this is the form of loading that emits a SELECT statement at attribute access time to lazily load a related reference on a single object at a time. 

JOINED LOADING -

available via lazy='joined' or the joinedload() option, 
this form of loading applies a JOIN to the given SELECT statement so that related rows are loaded in the same result set. 

SUBQUERY LOADING -

available via lazy='subquery' or the subqueryload() option,
this form of loading emits a second SELECT statement which re-states the original query embedded inside of a subquery,
then JOINs that subquery to the related table to be loaded to load all members of related collections / scalar references at once.

SELECT IN LOADING - 

available via lazy='selectin' or the selectinload() option,
this form of loading emits a second (or more) SELECT statement which assembles the primary key identifiers of the parent objects into an IN clause,
so that all members of related collections / scalar references are loaded at once by primary key.

RAISE LOADING -

available via lazy='raise', lazy='raise_on_sql', or the raiseload() option,
this form of loading is triggered at the same time a lazy load would normally occur,
except it raises an ORM exception in order to guard against the application making unwanted lazy loads.
An introduction to raise loading is at Preventing unwanted lazy loads using raiseload.

NO LOADING -

available via lazy='noload', or the noload() option;
this loading style turns the attribute into an empty attribute (None or []) that will never load or have any loading effect.
This seldom-used strategy behaves somewhat like an eager loader when objects are loaded in that an empty attribute or collection is placed,
but for expired objects relies upon the default value of the attribute being returned on access; 
the net effect is the same except for whether or not the attribute name appears in the InstanceState.unloaded collection.
noload may be useful for implementing a “write-only” attribute but this usage is not currently tested or formally supported.
'''
'''
---------------------------------------------SQLAlchemy Core queries for specific queries-------------------------------

SELECT

>>> select_stmt=(db.select(Person.name).where(Person.name=='Prateek'))
>>> print(select_stmt)
SELECT person.name 
FROM person 
WHERE person.name = :name_1
>>> results=db.session.execute(select_stmt)
2022-09-11 19:20:17,560 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-09-11 19:20:17,562 INFO sqlalchemy.engine.Engine SELECT person.name 
FROM person 
WHERE person.name = ?
2022-09-11 19:20:17,562 INFO sqlalchemy.engine.Engine [generated in 0.00024s] ('Prateek',)

'''

