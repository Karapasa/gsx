from flask import Flask
from config import BaseConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
loginmanager = LoginManager(app)
loginmanager.login_view = 'login'
app.config.from_object(BaseConfig)

from app import views, models
