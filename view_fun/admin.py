from flask import Blueprint
from flask import request
from flask import render_template
from flask_wtf import Form
from wtforms import TextAreaField
from wtforms import StringField
from wtforms.validators import DataRequired

admin_blueprint = Blueprint(
	'admin',
	__name__,
	url_prefix='/admin'
	)

class MyBlogEdit(Form):
	title = StringField('Title', validators=[DataRequired()])
	text = TextAreaField("Text", validators=[DataRequired()])

@admin_blueprint.route('/', methods=['GET', 'POST'])
def index():
	form = MyBlogEdit()
	if form.validate_on_submit():
		print(form.title)
	return render_template('admin/admin.html', form=form)

@admin_blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
	print('dsadasdasdad')
	return render_template('admin/admin.html', form=form)

@admin_blueprint.route('/add', methods=['GET', 'POST'])
def add():
	form = request.form
	print(form)
	return 'hello'