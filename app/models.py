# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from app import db


class User(db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    user        = db.Column(db.String(64), unique = True)
    password    = db.Column(db.String(500))
    name        = db.Column(db.String(500))
    email       = db.Column(db.String(120), unique = True)

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

    # only if you want to have another table name mapped over this model 
    #__tablename__ = "Object"
    
    id          = db.Column(db.Integer, primary_key=True)
    userid      = db.Column(db.Integer)
    key1        = db.Column(db.String(100))
    key1_q      = db.Column(db.Integer)
    key2        = db.Column(db.String(100))
    key2_q      = db.Column(db.Integer)
    key3        = db.Column(db.String(100))
    key3_q      = db.Column(db.Integer)
    key4        = db.Column(db.String(100))
    key4_q      = db.Column(db.Integer)
    key5        = db.Column(db.String(100))
    key5_q      = db.Column(db.Integer)
    key6        = db.Column(db.String(100))
    key6_q      = db.Column(db.Integer)
    key7        = db.Column(db.String(100))
    key7_q      = db.Column(db.Integer)
    key8        = db.Column(db.String(100))
    key8_q      = db.Column(db.Integer)
    key9        = db.Column(db.String(100))
    key9_q      = db.Column(db.Integer)
    key10       = db.Column(db.String(100))
    key10_q     = db.Column(db.Integer)
    data1       = db.Column(db.String(500))
    data1_q     = db.Column(db.Integer)
    data2       = db.Column(db.String(500))
    data2_q     = db.Column(db.Integer)
    data3       = db.Column(db.String(500))
    data3_q     = db.Column(db.Integer)
    data4       = db.Column(db.String(500))
    data4_q     = db.Column(db.Integer)
    data5       = db.Column(db.String(500))
    data5_q     = db.Column(db.Integer)
    data6       = db.Column(db.String(500))
    data6_q     = db.Column(db.Integer)
    data7       = db.Column(db.String(500))
    data7_q     = db.Column(db.Integer)
    data8       = db.Column(db.String(500))
    data8_q     = db.Column(db.Integer)
    data9       = db.Column(db.String(500))
    data9_q     = db.Column(db.Integer)
    data10      = db.Column(db.String(500))
    data10_q    = db.Column(db.Integer)
    rawdata     = db.Column(db.String(5000))
    rawdata_q   = db.Column(db.Integer)
    lastupdate  = db.Column(db.Integer)

    def __init__(self):
        self.userid     = -1
        self.key1       = None
        self.key1_q     = -1
        self.key2       = None
        self.key2_q     = -1
        self.key3       = None
        self.key3_q     = -1
        self.key4       = None
        self.key4_q     = -1
        self.key5       = None
        self.key5_q     = -1
        self.key6       = None
        self.key6_q     = -1
        self.key7       = None
        self.key7_q     = -1
        self.key8       = None
        self.key8_q     = -1
        self.key9       = None
        self.key9_q     = -1
        self.key10      = None
        self.key10_q    = -1
        self.data1      = None
        self.data1_q    = -1
        self.data2      = None
        self.data2_q    = -1
        self.data3      = None
        self.data3_q    = -1
        self.data4      = None
        self.data4_q    = -1
        self.data5      = None
        self.data5_q    = -1
        self.data6      = None
        self.data6_q    = -1
        self.data7      = None
        self.data7_q    = -1
        self.data8      = None
        self.data8_q    = -1
        self.data9      = None
        self.data9_q    = -1
        self.data10     = None
        self.data10_q   = -1
        self.rawdata    = None
        self.rawdata_q  = -1
        self.lastupdate = -1
    
        def __repr__(self):
            return 'dummy ... Object'
