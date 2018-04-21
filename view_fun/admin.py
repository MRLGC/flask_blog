from flask import Blueprint
from flask import request
from flask import render_template
from wtforms import SelectField
from forms.edit import MyBlogEdit
from models.topic import Topics
from models.tags import Tags
import uuid
from models import db

admin_blueprint = Blueprint(
	'admin',
	__name__,
	url_prefix='/admin'
	)

# @admin_blueprint.route('')


@admin_blueprint.route('/', methods=['GET', 'POST'])
def index():
	t = Tags().query.all()
	tags = []
	for i in t:
		tags.append((i.tag_name, i.tag_name))
	MyBlogEdit.tags = SelectField('Tag', choices=tags) 
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
	topic = Topics()
	# topic.author_id = 2
	# topic.content = form.get('text')
	# topic.title = form.get("title") 
	# topic.tag_id = 1
	# db.session.add(topic)
	# db.session.commit()
	# return render_template('index/index.html')