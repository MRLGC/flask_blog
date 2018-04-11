from models import db

class Tags(db.Model):

	__tablename__ = 'tags'
	id = db.Column(db.Integer, primary_key=True)
	tag_name = db.Column(db.String(20))
	topic = db.relationship(
		'Topics',
		backref='tag',
		lazy='dynamic',
	)

	def __repr__(self):
		return '<Tag {}>',format(self.tag_name)