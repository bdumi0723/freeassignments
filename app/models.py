# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from app import db

class ModelExample(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(250))
	content = db.Column(db.Text)
	date = db.Column(db.DateTime)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(500))
    name = db.Column(db.String(500))
    email = db.Column(db.String(120), unique = True)
    # posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=True)
    key1 = db.Column(db.String(100))
    key1_q = db.Column(db.Integer)
    key2 = db.Column(db.String(100))
    key2_q = db.Column(db.Integer)
    key3 = db.Column(db.String(100))
    key3_q = db.Column(db.Integer)
    key4 = db.Column(db.String(100))
    key4_q = db.Column(db.Integer)
    key5 = db.Column(db.String(100))
    key5_q = db.Column(db.Integer)
    key6 = db.Column(db.String(100))
    key6_q = db.Column(db.Integer)
    key7 = db.Column(db.String(100))
    key7_q = db.Column(db.Integer)
    key8 = db.Column(db.String(100))
    key8_q = db.Column(db.Integer)
    key9 = db.Column(db.String(100))
    key9_q = db.Column(db.Integer)
    key10 = db.Column(db.String(100))
    key10_q = db.Column(db.Integer)
    data1 = db.Column(db.String(500))
    data1_q = db.Column(db.Integer)
    data2 = db.Column(db.String(500))
    data2_q = db.Column(db.Integer)
    data3 = db.Column(db.String(500))
    data3_q = db.Column(db.Integer)
    data4 = db.Column(db.String(500))
    data4_q = db.Column(db.Integer)
    data5 = db.Column(db.String(500))
    data5_q = db.Column(db.Integer)
    data6 = db.Column(db.String(500))
    data6_q = db.Column(db.Integer)
    data7 = db.Column(db.String(500))
    data7_q = db.Column(db.Integer)
    data8 = db.Column(db.String(500))
    data8_q = db.Column(db.Integer)
    data9 = db.Column(db.String(500))
    data9_q = db.Column(db.Integer)
    data10 = db.Column(db.String(500))
    data10_q = db.Column(db.Integer)
    rawdata = db.Column(db.String(5000))
    rawdata_q = db.Column(db.Integer)
    lastupdate = db.Column(db.Integer)
    
