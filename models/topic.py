from models import db

class Topics(db.Model):

	__tablename__ = 'topics'
	title = db.Column(db.String(50))
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	author_id = db.Column(db.Integer)
	tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
	
	
	def __repr__(self):
		return "<Topic {}>".format(self.title)
 



