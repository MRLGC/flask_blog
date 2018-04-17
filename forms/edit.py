from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import StringField
from wtforms import SelectField
from wtforms.validators import DataRequired

class MyBlogEdit(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	text = TextAreaField("Text", validators=[DataRequired()])
	tags = None
	def __init__(self, ls):
		super().__init__()
		tags = []
		for i in ls:
			tags.append((i.tag_name, i.tag_name))
		self.tags = SelectField('Tags', choices=tags)

