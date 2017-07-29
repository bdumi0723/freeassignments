# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
from flask_wtf          	 import Form
from flask_wtf.file          import FileRequired
from wtforms            	 import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators		 import InputRequired, Email, DataRequired

class NewAssignmentForm(Form):
	title       = StringField('Title'			, [DataRequired(), InputRequired()])
	info        = StringField('Info'			, [DataRequired(), InputRequired()])
	description = StringField('Description'		, [DataRequired(), InputRequired()])
	tags        = StringField('Tags'			, [DataRequired(), InputRequired()])
	file        = FileField  ('Assignment'		, [FileRequired()])#, Regexp('(\.{1}(zip|rar))$', message='File must be zip or rar')])

	