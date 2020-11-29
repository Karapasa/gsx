from flask import render_template
from . import err


@err.app_errorhandler(404)
def not_found_error(error):
    return render_template('page_404.html'), 404
