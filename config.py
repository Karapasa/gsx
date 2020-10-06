import os


class BaseConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gsx_db:gsxdbpass@localhost/gsx_db'
    SQLALCHEMY_TRACK_MODIFICATION = False