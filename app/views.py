# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

import re, os
from flask import url_for, redirect, render_template, flash, g, session, jsonify, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app
from app.models import Object
from forms import NewAssignmentForm
from models import User
from app import db

# App Entry point ..
@app.route('/')
def index():
    return render_template('index.html')

# Add another assignment
@app.route('/add_assignment', methods=['GET', 'POST'])
def add_assignment():

    form = NewAssignmentForm()

    submit = request.form.get('submit', None, type=str)

    # POST ..
    if submit:
        if not form.validate():
            return 'Submission failed'
        title = request.form.get('title',        '', type=str)
        info  = request.form.get('info',         '', type=str)
        desc  = request.form.get('description',  '', type=str)
        tags  = request.form.get('tags',         '', type=str)
        file  = form.file.data

        if not re.match("(.+\.{1}(zip|rar)$)", str(file.filename)):
            return 'File type unsupported'
        #else:
        #    return 'OK'
        file.save(os.path.join(os.getcwd(), 'uploads', file.filename))
        #file.save(os.path.join('/home', 'ginfuu', 'uploads', file.filename))
        obj      = Object()
        obj.key1 = title ;
        obj.key2 = info  ;
        obj.key3 = desc  ;
        obj.key4 = tags  ;
        obj.key5 = file.filename;

        db.session.add   ( obj ); # open transaction 
        db.session.commit(     ); # save

        return 'Save ok: ' + str( obj.id )

    # On GET we display the form ..         
    else:    
        return render_template('common/add_assignment.html',
                                form=form)

# View assignment
@app.route('/view_assignment', methods=['GET'])
def view_assignment():
    c
    return render_template('common/view_assignment.html',
                            assign_id=assign_id)

# TESTING ONLY --------------------------------
# Usefull ONLY to check out the theme
# Functionally deprecated in production !!!
# ---------------------------------------------
@app.route('/theme')
def index_old():
    return render_template('theme.html')

# TESTING ONLY --------------------------------
# Check Ajax comm
# Functionally deprecated in production !!!
# ---------------------------------------------
@app.route('/oper_numbers', methods = ['POST'])
def add_numbers():
    a    = request.form.get('a'   , 0    , type=int)
    b    = request.form.get('b'   , 0    , type=int)
    oper = request.form.get('oper', 'add', type=str)

    if oper == "add":
        return jsonify(result=a + b)

    if oper == "multiply":
        return jsonify(result=a * b)
    
    return jsonify(result='oper err: ' + oper)

# TESTING ONLY --------------------------------
# List all db ..
# Functionally deprecated in production !!!
# ---------------------------------------------
@app.route('/list_db')
def list_db():

    objects = Object.query.all()

    return render_template("common/list_db.html",
                           objects=Object.query.all())

# ====================
