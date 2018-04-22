from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from wtforms import SelectField
from forms.edit import MyBlogEdit
from forms.login import Login
from models.topic import Topics
from models.tags import Tags
from models.users import Users
import uuid
from models import db
from flask_login import LoginManager
from flask_login import login_user
from flask_login import login_required


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