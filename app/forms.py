# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
from flask_wtf          import Form
from wtforms            import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email, DataRequired

class NewAssignmentForm(Form):
	title       = StringField(u'Title'			, validators=[DataRequired()])
	info        = StringField(u'Info'			, validators=[DataRequired()])
	description = StringField(u'Description'	, validators=[DataRequired()])
	tags        = StringField(u'Tags'			, validators=[DataRequired()])
