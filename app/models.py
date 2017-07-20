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

    __tablename__ = "Obj"
    
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
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

    def __init__(self, userid, key1, key1_q, key2, key2_q, key3, key3_q, key4,
        key4_q, key5, key5_q, key6, key6_q, key7, key7_q, key8, key8_q, key9,
        key9_q, key10, key10_q, data1, data1_q, data2, data2_q, data3, data3_q,
        data4, data4_q, data5, data5_q, data6, data6_q, data7, data7_q, data8,
        data8_q, data9, data9_q, data10, data10_q, rawdata, rawdata_q, lastupdate):
        self.userid = userid
        self.key1 = key1
        self.key1_q = key1_q
        self.key2 = key2
        self.key2_q = key2_q
        self.key3 = key3
        self.key3_q = key3_q
        self.key4 = key4
        self.key4_q = key4_q
        self.key5 = key5
        self.key5_q = key5_q
        self.key6 = key6
        self.key6_q = key6_q
        self.key7 = key7
        self.key7_q = key7_q
        self.key8 = key8
        self.key8_q = key8_q
        self.key9 = key9
        self.key9_q = key9_q
        self.key10 = key10
        self.key10_q = key10_q
        self.data1 = data1
        self.data1_q = data1_q
        self.data2 = data2
        self.data2_q = data2_q
        self.data3 = data3
        self.data3_q = data3_q
        self.data4 = data4
        self.data4_q = data4_q
        self.data5 = data5
        self.data5_q = data5_q
        self.data6 = data6
        self.data6_q = data6_q
        self.data7 = data7
        self.data7_q = data7_q
        self.data8 = data8
        self.data8_q = data8_q
        self.data9 = data9
        self.data9_q = data9_q
        self.data10 = data10
        self.data10_q = data10_q
        self.rawdata = rawdata
        self.rawdata_q = rawdata_q
        self.lastupdate = lastupdate
    
