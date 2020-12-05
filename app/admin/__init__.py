from flask import Blueprint

admin_panel = Blueprint('admin', __name__)

from . import views