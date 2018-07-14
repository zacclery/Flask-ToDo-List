import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
