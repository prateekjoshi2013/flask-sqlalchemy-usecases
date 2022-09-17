from pickle import TRUE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    name = db.Column(db.String(50))


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    name = db.Column(db.String(50))
    salary = db.Column(db.Integer)

# select_from is used to determine the left table
'''
db.create_all()

companies=['A','B','C']
departments=['Human Recource','Accounting','Sales','Engineering']
employees=['Paul','John','Jane']
for i in range(len(companies)):
    company=Company(name=f'Company-{companies[i]}')
    db.session.add(company)
    db.session.commit() 
    for j in range(len(departments)):
        department=Department(name=departments[j],company_id=company.id)
        db.session.add(department)
        db.session.commit()
        for  k in range(len(employees)):
            employee=Employee(name=employees[k],salary=1000,department_id=department.id)
            db.session.add(employee)
            db.session.commit() 

results=db.session.query(
    Employee.id,Employee.name,Employee.salary,Department.name.label('department'),Company.name.label('company')
    ).select_from(Employee).join(Department).join(Company).all()

>>> print(results)
[(1, 'Paul', 1000, 'Human Recource', 'Company-A'),
 (2, 'John', 1000, 'Human Recource', 'Company-A'),
  (3, 'Jane', 1000, 'Human Recource', 'Company-A'),
   (4, 'Paul', 1000, 'Accounting', 'Company-A'),
    (5, 'John', 1000, 'Accounting', 'Company-A'),
     (6, 'Jane', 1000, 'Accounting', 'Company-A'),
      (7, 'Paul', 1000, 'Sales', 'Company-A'),
       (8, 'John', 1000, 'Sales', 'Company-A'),
        (9, 'Jane', 1000, 'Sales', 'Company-A'),
         (10, 'Paul', 1000, 'Engineering', 'Company-A'),
          (11, 'John', 1000, 'Engineering', 'Company-A'),
           (12, 'Jane', 1000, 'Engineering', 'Company-A'),
            (13, 'Paul', 1000, 'Human Recource', 'Company-B'),
             (14, 'John', 1000, 'Human Recource', 'Company-B'),
              (15, 'Jane', 1000, 'Human Recource', 'Company-B'),
               (16, 'Paul', 1000, 'Accounting', 'Company-B'),
                (17, 'John', 1000, 'Accounting', 'Company-B'),
                 (18, 'Jane', 1000, 'Accounting', 'Company-B'),
                  (19, 'Paul', 1000, 'Sales', 'Company-B'),
                   (20, 'John', 1000, 'Sales', 'Company-B'),
                    (21, 'Jane', 1000, 'Sales', 'Company-B'),
                     (22, 'Paul', 1000, 'Engineering', 'Company-B'),
                      (23, 'John', 1000, 'Engineering', 'Company-B'),
                       (24, 'Jane', 1000, 'Engineering', 'Company-B'),
                        (25, 'Paul', 1000, 'Human Recource', 'Company-C'),
                         (26, 'John', 1000, 'Human Recource', 'Company-C'),
                          (27, 'Jane', 1000, 'Human Recource', 'Company-C'),
                           (28, 'Paul', 1000, 'Accounting', 'Company-C'),
                            (29, 'John', 1000, 'Accounting', 'Company-C'),
                             (30, 'Jane', 1000, 'Accounting', 'Company-C'),
                              (31, 'Paul', 1000, 'Sales', 'Company-C'),
                               (32, 'John', 1000, 'Sales', 'Company-C'),
                                (33, 'Jane', 1000, 'Sales', 'Company-C'),
                                 (34, 'Paul', 1000, 'Engineering', 'Company-C'),
                                  (35, 'John', 1000, 'Engineering', 'Company-C'),
                                   (36, 'Jane', 1000, 'Engineering', 'Company-C')]
'''

