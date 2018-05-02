import os
class Config(object):
    SECRET_KEY = 'you never get'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CKEDITOR_FILE_UPLOADER = 'admin.upload'
 
class ProdConfig(Config):
    env = os.environ
    SQLALCHEMY_DATABASE_URI = env.get('MYSQLCONNECTOR')

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'