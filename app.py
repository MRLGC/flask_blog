from flask import Flask
from view_fun.index import index_blueprint as index
from flask_bootstrap import Bootstrap
from view_fun.admin import admin_blueprint as admin
from models.topic import db
app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)
db.init_app(app)
app.register_blueprint(index)
app.register_blueprint(admin)

@app.before_request
def create_data():
	db.create_all()

if __name__ == '__main__':
	app.run(port=5000,debug=True)