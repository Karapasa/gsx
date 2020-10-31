import os
basesir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gsx_db:gsxdbpass@localhost/gsx_db'
    SQLALCHEMY_TRACK_MODIFICATION = False
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_TSL = True
    MAIL_USERNAME = 'alexmixpetrov@yandex.ru'
    MAIL_PASSWORD = '03Dik0braZ02'
    MAIL_DEFAULT_SENDER = 'alexmixpetrov@yandex.ru'


class TestConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basesir, 'testdb.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_TSL = True
    MAIL_USERNAME = 'alexmixpetrov@yandex.ru'
    MAIL_PASSWORD = '03Dik0braZ02'
    MAIL_DEFAULT_SENDER = 'alexmixpetrov@yandex.ru'
