from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from models.users import Users
from models import db
import hashlib

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('submit')

    def is_correct(self, username, password):
        u = db.session.query(Users).filter_by(user_name=username).one()
        md5 = hashlib.md5()
        md5.update(password.encode('utf8'))
        if u and (u.password == md5.hexdigest()):
            return u
        else:
            return None

