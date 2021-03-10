from flask import Flask
from config import BaseConfig, TestConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_babel import Babel

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
loginmanager = LoginManager()
loginmanager.login_view = 'auth.login'
mail = Mail()
babel = Babel()


def create_app(config_class=TestConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    loginmanager.init_app(app)
    mail.init_app(app)
    babel.init_app(app)

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    from .errors import err as err_bp
    app.register_blueprint(err_bp)

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from .admin import admin_panel as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from .api import api as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
