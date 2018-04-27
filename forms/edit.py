from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import StringField
from wtforms import SelectField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from models.tags import Tags
from flask_ckeditor import CKEditorField

class MyBlogEdit(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	submit = SubmitField('提交')
	ckeditor = CKEditorField('Text', validators=[DataRequired()])
	def __setattr__(self, name, value):
		super().__setattr__(name, value)
