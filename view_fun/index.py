import os
import random
import copy

from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import send_from_directory
from flask import abort
from models.topic import Topics
from models.tags import Tags


index_blueprint = Blueprint(
	'index',
	__name__,
	)

basedir = os.path.dirname(os.path.abspath(__name__))


@index_blueprint.route('/',methods=['GET'])
def index():
	topicList = Topics.get_topic_sum(basedir)
	return render_template('index/index.html', topicList=topicList)

@index_blueprint.route('/archives',methods=['GET'])
def archives():
	topic = Topics()
	topicList = topic.query.order_by('createTime').all()
	return render_template('index/archives.html', topicList=topicList)

@index_blueprint.route('/tags',methods=['GET'])
def tags():
	tag = Tags()
	tagList = tag.query.all()
	return render_template('index/tags.html', tagList=tagList)

@index_blueprint.route('/about',methods=['GET'])
def about():
	return render_template('index/about.html')

@index_blueprint.route('/topic/<topicId>',methods=['GET'])
def detail(topicId):
	topic = Topics()
	topicObj = topic.query.filter_by(id=topicId).first()
	if topicObj:
		tags = topicObj.tag
		reconTopic = tags.topic.limit(4)
		return render_template('index/detail.html', topicObj=topicObj, reconTopic=reconTopic)
	else:
		return abort(404)

@index_blueprint.route('/pic/<file>',methods=['GET'])
def picLoad(file):
	uploaddir = os.path.join(basedir, 'static/img/randomPic')
	return send_from_directory(uploaddir, file)

@index_blueprint.route('/favicon.ico', methods=['GET'])
def icon():
	uploaddir = os.path.join(basedir, 'static/img/webHeaderPic')
	return send_from_directory(uploaddir, 'doge.jpg')

@index_blueprint.route('/aboutPic', methods=['GET'])
def aboutPic():
	uploaddir = os.path.join(basedir, 'static/img/adminPic')
	return send_from_directory(uploaddir, 'personalPic.png')

