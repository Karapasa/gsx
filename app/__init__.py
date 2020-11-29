from flask import Flask
from config import BaseConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
loginmanager = LoginManager()
loginmanager.login_view = 'main.login'
mail = Mail()


def create_app(config_class=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    loginmanager.init_app(app)
    mail.init_app(app)

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    return app
