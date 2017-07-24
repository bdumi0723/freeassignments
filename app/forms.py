# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Email

class ExampleForm(Form):
	content = StringField(u'Conteúdo')
	#date = DateTimeField(u'Data', format='%d/%m/%Y %H:%M')
	#recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(Form):
	user = StringField(u'User', validators = [InputRequired()])
	password = StringField(u'Pass', validators = [InputRequired()])
	
class MyForm2(Form):
	n1 = IntegerField('n1', validators=[InputRequired()]
	n2 = IntegerField('n2', validators=[InputRequired()]
