from string import ascii_lowercase
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from string import ascii_lowercase
from random import choices, choice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kenrbogn:s7pyZ-IYU2MgZutBJzTcXOrQHULh6HTP@jelani.db.elephantsql.com/kenrbogn'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class TableWithJsonCol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json_column = db.Column(JSON)


def insert_students():
    students = []
    for i in range(5):
        marks = [12, 32, 13, 4, 15, 20]
        ages = [4, 3, 5, 2, 6, 10]
        subject_marks = []
        for i in range(5):
            subject = ''.join(choices(ascii_lowercase, k=5))
            subject_marks.append({'subject': subject, 'score': choice(marks)})
        student_name = ''.join(choices(ascii_lowercase, k=10))
        student_age = choice(ages)
        student = TableWithJsonCol(
            json_column={'type': 'Student',
                         'details': {
                             'name': student_name,
                             'age': student_age
                         },
                         'marks': subject_marks})
        students.append(student)
    db.session.add_all(students)
    db.session.commit()


def insert_employees():
    employees = []
    for i in range(5):
        grades = ['A', 'B', 'C', 'D']
        ages = [24, 32, 50, 28, 62, 40]
        salaries = [5000, 4000, 3000, 2000, 6000]
        name = ''.join(choices(ascii_lowercase, k=10))
        employee = TableWithJsonCol(
            json_column={'type': 'Employee',
                         'details': {
                             'name': name,
                             'age': choice(ages),
                             'grade': choice(grades),
                             'salary': choice(salaries),
                         }, })
        employees.append(employee)
    db.session.add_all(employees)
    db.session.commit()


def query_employees():
    employees = TableWithJsonCol.query.filter(
        TableWithJsonCol.json_column['type'].astext == 'Employee').filter(
            TableWithJsonCol.json_column['details']['salary'].astext.cast(db.Integer) > 3000).all()
    print(employees)

def query_students():
    employees = db.session.query(TableWithJsonCol.json_column['details']['name'].astext,TableWithJsonCol.json_column['details']['salary'].astext.cast(db.Integer)).all()
    print(employees)
    employees_total_salary = db.session.query(db.func.sum(TableWithJsonCol.json_column['details']['salary'].astext.cast(db.Integer))).sacalar()
    print(employees_total_salary)