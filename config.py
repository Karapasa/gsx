import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class BaseConfig(object):
    FLASK_APP = os.getenv("FLASK_APP")
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATION = False
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')
    BABEL_DEFAULT_LOCALE = os.getenv('BABEL_DEFAULT_LOCALE')
    BABEL_DEFAULT_TIMEZONE = os.getenv('BABEL_DEFAULT_TIMEZONE')


class TestConfig(BaseConfig):
    DEBUG = True
    FLASK_DEBUG = 1
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'testdb.db')
    SQLALCHEMY_TRACK_MODIFICATION = True
