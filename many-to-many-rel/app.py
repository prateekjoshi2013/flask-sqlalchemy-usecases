from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

person_channel = db.Table('person_channel',
                          db.Column('person_id', db.Integer,
                                    db.ForeignKey('person.id')),
                          db.Column('channel_id', db.Integer,
                                    db.ForeignKey('channel.id'))
                          )


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    following = db.relationship(
        'Channel', secondary=person_channel, backref='followers')

    def __repr__(self) -> str:
        return f'Person < id: {self.id} name: {self.name} >'


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self) -> str:
        return f'Channel < id: {self.id} name: {self.name} >'

db.create_all()