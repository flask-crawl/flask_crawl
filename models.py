# -*- coding: utf-8 -*-

from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(50),nullable=False)

    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    
class Adcode(db.Model):
    __tablename__ = 'adcode'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    city = db.Column(db.String(50),nullable=False)
    adcode = db.Column(db.Integer,nullable=False)
    
class Scenecode(db.Model):
    __tablename__ = 'scenecode'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    scene = db.Column(db.String(50),nullable=False)
    scenecode = db.Column(db.Integer,nullable=False)

class Dataoperation(db.Model):
    __tablename__ = 'dataoperation'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    city = db.Column(db.String(50),nullable=False)
    adcode = db.Column(db.Integer,nullable=False)
    scene = db.Column(db.String(50),nullable=False)
    scenecode = db.Column(db.Integer,nullable=False)
    adsl_server_url = db.Column(db.String(50),nullable=False)
    adsl_server_auth = db.Column(db.String(50),nullable=False)
    key = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    
#    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
#    
#    author = db.relationship('User',backref=db.backref('database'))
    