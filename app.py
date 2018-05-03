from flask import Flask
from view_fun.index import index_blueprint as index
from flask_bootstrap import Bootstrap
from view_fun.admin import admin_blueprint as admin
from models import db
from view_fun.admin import login_opt
from view_fun.admin import ckeditor
from config import DevConfig, ProdConfig
import platform
def createApp():
	app = Flask(__name__)
	sysstr = platform.system()
	if sysstr == 'Linux':
		app.config.from_object(ProdConfig)
	else:
		app.config.from_object(DevConfig)
	Bootstrap(app)
	db.init_app(app)
	ckeditor.init_app(app)
	login_opt.init_app(app)
	app.register_blueprint(index)
	app.register_blueprint(admin)
	@app.before_request
	def create_data():
		db.create_all()
	if not app.debug:
		import logging
		from logging.handlers import RotatingFileHandler
		fileHandler = RotatingFileHandler('logfile/Myblog.log', mode='a', maxBytes=1*1024*1024, backupCount=10)
		formatStr = '%(asctime)s %(levelname)s: %(message)s [%(pathname)s:%(lineno)d]'
		logFormate = logging.Formatter(formatStr)
		fileHandler.setFormatter(logFormate)
		app.logger.setLevel(logging.INFO)
		fileHandler.setLevel(logging.INFO)
		app.logger.addHandler(fileHandler)
		app.logger.info('Myblog startup')
	return app
	
if __name__ == '__main__':
	app = createApp()
	app.run(port=5300,debug=True,host='0.0.0.0')