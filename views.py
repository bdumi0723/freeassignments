# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session
from flask_login import login_user, logout_user, current_user, login_required
from app import app, lm
from app.models import Object
from forms import ExampleForm, LoginForm, MyForm2
from models import User
from app import db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/old')
def index_old():
    return render_template('index_old.html')

@app.route('/list/')
def posts():
    return render_template('list.html')

@app.route('/new/')
@login_required
def new():
    form = ExampleForm()
    return render_template('new.html', form=form)

@app.route('/save/', methods = ['GET','POST'])
@login_required
def save():
    form = ExampleForm()
    if form.validate_on_submit():
        print "salvando os dados:"
        print form.title.data
        print form.content.data
        print form.date.data
        flash('Dados salvos!')
    return render_template('new.html', form=form)

@app.route('/view/<id>/')
def view(id):
    return render_template('view.html')

# === User login methods ===

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/form_1/', methods = ['GET', 'POST'])
def myform():
    form = MyForm()
    if form.validate_on_submit():
        return 'The result is %r' %(form.number1.data * form.number2.data)
    return render_template('myform.html',title = 'MyFrom', form = form)

@app.route('/form_2', methods = ['GET', 'POST'])
def myform2():
    form = MyForm2()
    if form.validate_on_submit():
        return "Rezultatul este %r" % (form.n1.data * form.n2.data)
    return render_template('myform2.html', form=form)


@app.route('/get_table/')

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        login_user(g.user)

    return render_template('login.html', 
        title = 'Sign In',
        form = form)

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/table')
def testdb():
    data1 = Object(2,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,0)
    data2 = Object(3,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,'0',0,0)
    
    db.session.add(data1)
    db.session.add(data2)
    db.session.commit()

    results = Object.query.all()

    string = ''

    for result in results:
        string = string + str(result.id) + ' '
    return string

# ====================
