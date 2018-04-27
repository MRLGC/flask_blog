from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import send_from_directory
from flask import abort
from models.topic import Topics
import os
import random
index_blueprint = Blueprint(
	'index',
	__name__,
	)

@index_blueprint.route('/',methods=['GET'])
def index():
	topic = Topics()
	topicList = topic.query.order_by('createTime').limit(4)
	basedir = os.path.dirname(os.path.abspath(__name__))
	path = os.path.join(basedir, 'static/img/randomPic')
	picLs = os.listdir(path)
	ranPicLs = random.sample(picLs, 4)
	for i, p in zip(topicList, ranPicLs):
		i.pic_url = p
	return render_template('index/index.html', topicList=topicList)

@index_blueprint.route('/archives',methods=['GET'])
def archives():
	topic = Topics()
	topicList = topic.query.order_by('createTime').all()
	return render_template('index/archives.html', topicList=topicList)

@index_blueprint.route('/tags',methods=['GET'])
def tags():
	return render_template('index/tags.html')

@index_blueprint.route('/about',methods=['GET'])
def about():
	return render_template('index/about.html')

@index_blueprint.route('/topic',methods=['GET'])
def detail():
	topic = Topics()
	# topicObj = topic.query.filter_by(id=topicId).first()
	if True:
		return render_template('index/detail.html')
	else:
		return abort(404)

@index_blueprint.route('/pic/<file>',methods=['GET'])
def picLoad(file):
	basedir = os.path.dirname(os.path.abspath(__name__))
	uploaddir = os.path.join(basedir, 'static/img/randomPic')
	return send_from_directory(uploaddir, file)

