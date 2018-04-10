from flask import Flask
from view_fun.index import index_blueprint as index
from flask_bootstrap import Bootstrap
from view_fun.admin import admin_blueprint as admin
from models.topic import db
app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)
app.register_blueprint(index)
app.register_blueprint(admin)

if __name__ == '__main__':
	app.run(port=8017,debug=True)