from flask import Blueprint
from flask import render_template

index_blueprint = Blueprint(
	'index',
	__name__,
	# url_prefix='/'
	)

@index_blueprint.route('/',methods=['GET'])
def index():
	return render_template('index/index.html')

@index_blueprint.route('/archives',methods=['GET'])
def archives():
	return render_template('index/archives.html')

@index_blueprint.route('/tags',methods=['GET'])
def tags():
	return render_template('index/tags.html')

@index_blueprint.route('/about',methods=['GET'])
def about():
	return render_template('index/about.html')
