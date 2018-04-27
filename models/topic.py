from models import db
from models import tags
import datetime

class Topics(db.Model):

	__tablename__ = 'topics'
	title = db.Column(db.String(50))
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	author_id = db.Column(db.Integer)
	tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
	pic_url = db.Column(db.String(200))
	createTime = db.Column(db.DateTime)
	
	def __init__(self):
		self.createTime = datetime.datetime.now()
		self.author_id = '1'


	def __repr__(self):
		return "<Topic {}>".format(self.title)
 

