from models import db
from hashlib import md5


class Users(db.Model):

    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, name, pd):
        self.user_name = name
        self.password = self.hashPassword(pd)

    def hashPassword(self, pd):
        md5 = md5.update(pd)
        return md5.hexdigest()
    
    def __repr__(self):
        return '<User {}>'.format(self.name)

    
