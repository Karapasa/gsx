from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.admin.forms import AdminsPost
from app.models import Owner, create_post
from . import admin_panel


@admin_panel.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    form = AdminsPost()
    if form.validate_on_submit():
        create_post(form.data)
    if current_user.is_authenticated and db.session.query(Owner).filter(Owner.role == 1).first():
        return render_template('admin/admin.html', form=form)
    else:
        return redirect(url_for('auth.login'))
