from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import send_from_directory
from wtforms import SelectField
from forms.login import Login
from models.topic import Topics
from models.tags import Tags
from models.users import Users
from forms.edit import MyBlogEdit
from models import db
from flask_login import LoginManager
from flask_login import login_user
from flask_login import login_required
import os
from flask_ckeditor import CKEditor
ckeditor = CKEditor()
admin_blueprint = Blueprint(
	'admin',
	__name__,
	url_prefix='/admin'
	)
login_opt = LoginManager()
login_opt.login_manager = 'admin.login'
login_opt.session_protection = 'strong'
login_opt.login_message = "Please login to access this page."
# login_opt.login_message_category = 'info'
basedir = os.path.dirname(os.path.abspath(__name__))
def dynamicMyBlogEdit():
	t = Tags().query.all()
	tags = []
	for i in t:
		tags.append((i.id, i.tag_name))
	MyBlogEdit.tags = SelectField('Tag', choices=tags, coerce=int) 
	return MyBlogEdit


@login_opt.user_loader
def load_user(user_id):
	return Users.query.filter_by(id=user_id).first()


@admin_blueprint.route('/', methods=['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		user = form.is_correct(username, password)
		if user is not None:
			login_user(user)
			return redirect(url_for('admin.index'))
		else:
			return 'No Right To Get Into'
	return render_template('admin/login.html', form=form)


@admin_blueprint.route('/edit', methods=['GET', 'POST'])
@login_required
def index():
	MyBlog = dynamicMyBlogEdit()
	form = MyBlog()
	return render_template('admin/edit.html', form=form)

@admin_blueprint.route('/upload', methods=['POST'])
@login_required
@ckeditor.uploader
def upload():
	f = request.files.get('upload')
	uploaddir = os.path.join(basedir, 'uploadfile')
	f.save(os.path.join(uploaddir, f.filename))
	url = url_for('admin.files', filename=f.filename)
	return url

@admin_blueprint.route('/files/<filename>')
def files(filename):
	uploaddir = os.path.join(basedir, 'uploadfile')
	return send_from_directory(uploaddir, filename)

@admin_blueprint.route('/add', methods=['POST'])
@login_required
def add():
	MyBlog = dynamicMyBlogEdit()
	form = MyBlog()
	if form.validate_on_submit():
		topic = Topics()
		topic.title = form.title.data
		topic.content = form.ckeditor.data
		topic.tag_id = form.tags.data
		db.session.add(topic)
		db.session.commit()
		return redirect(url_for('admin.index'))
	else:
		return render_template('admin/edit.html', form=form)

@admin_blueprint.route('/topicList', methods=['GET'])
@login_required
def topicList():
	t = Tags()
	tagList = t.query.all()
	return render_template('admin/topicList.html', tagList=tagList)

@admin_blueprint.route('/delete/<topicId>', methods=['GET'])
@login_required
def delete(topicId):
	t = Topics()
	topic = t.query.filter_by(id=topicId).first()
	db.session.delete(topic)
	db.session.commit()
	return redirect(url_for('admin.topicList'))
