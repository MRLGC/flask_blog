import os
import datetime
import random

from models import db
from models import tags
from util.parse import parse_content

class Topics(db.Model):

	__tablename__ = 'topics'
	title = db.Column(db.String(50))
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	content_md = db.Column(db.Text)
	author_id = db.Column(db.Integer)
	tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
	pic_url = db.Column(db.String(200))
	createTime = db.Column(db.DateTime)
	
	def __init__(self):
		self.createTime = datetime.datetime.now()
		self.author_id = '1'

	@classmethod
	def get_topic_sum(cls, basedir):
		topic = cls.query.order_by(cls.createTime.desc()).limit(4)
		path = os.path.join(basedir, 'static/img/randomPic')
		picLs = os.listdir(path)
		ranPicLs = random.sample(picLs, 4)
		for i, p in zip(topic, ranPicLs):
			i.pic_url = p
			i.content = parse_content(i.content)
		return topic

	def __repr__(self):
		return "<Topic {}>".format(self.title)
 

