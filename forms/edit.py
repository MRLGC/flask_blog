from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import StringField
from wtforms import SelectField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from models.tags import Tags


class MyBlogEdit(FlaskForm):
	title = StringField('标题', validators=[DataRequired()])
	submit = SubmitField('提交')
	content = TextAreaField('文章内容', validators=[DataRequired()])
	
	def __setattr__(self, name, value):
		super().__setattr__(name, value)
