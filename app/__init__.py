from flask import Flask
from config import BaseConfig, TestConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
loginmanager = LoginManager(app)
loginmanager.login_view = 'login'
mail = Mail(app)
app.config.from_object(TestConfig)

from app import views, models
