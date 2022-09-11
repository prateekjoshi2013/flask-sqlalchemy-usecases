from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kenrbogn:s7pyZ-IYU2MgZutBJzTcXOrQHULh6HTP@jelani.db.elephantsql.com/kenrbogn'

db = SQLAlchemy(app)

# SCHEMA has to exist before running this code

# Gets created in public schema
class MyTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)

# Gets created in myschema schema
class MySecondTable(db.Model):
    __table_args__ = {'schema': 'myschema'}
    id = db.Column(db.Integer, primary_key=True)

# Gets created in public schema
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner', lazy='dynamic')

# Gets created in myschema schema
class Pet(db.Model):
    
    __table_args__ = {'schema': 'myschema'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))

db.create_all()

'''
Declarative Table Configuration

When using Declarative Table configuration with the __tablename__ declarative class attribute, 
additional arguments to be supplied to the Table constructor should be provided using the __table_args__ declarative class attribute.

This attribute accommodates both positional as well as keyword arguments that are normally sent to the Table constructor. 
The attribute can be specified in one of two forms. One is as a dictionary:

class MyClass(Base):
    __tablename__ = "sometable"
    __table_args__ = {"mysql_engine": "InnoDB"}
The other, a tuple, where each argument is positional (usually constraints):

class MyClass(Base):
    __tablename__ = "sometable"
    __table_args__ = (
        ForeignKeyConstraint(["id"], ["remote_table.id"]),
        UniqueConstraint("foo"),
    )
Keyword arguments can be specified with the above form by specifying the last argument as a dictionary:

class MyClass(Base):
    __tablename__ = "sometable"
    __table_args__ = (
        ForeignKeyConstraint(["id"], ["remote_table.id"]),
        UniqueConstraint("foo"),
        {"autoload": True},
    )

'''


# https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html#declarative-table-configuration