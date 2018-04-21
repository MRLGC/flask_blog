from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import StringField
from wtforms import SelectField
from wtforms.validators import DataRequired

class MyBlogEdit(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	text = TextAreaField("Text", validators=[DataRequired()])
	def __setattr__(self, name, value):
		super().__setattr__(name, value)
	

