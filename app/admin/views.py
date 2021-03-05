from functools import wraps

from flask import render_template, redirect, url_for
from flask_login import current_user

from app import db
from app.admin.forms import AdminsPost
from app.models import Owner, Post, Indicator
from . import admin_panel


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated and db.session.query(Owner).filter(
                Owner.id == current_user.id).first().role == 1:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('auth.login'))

    return wrapper


@admin_panel.route('/admin', methods=['GET', 'POST'])
@admin_required
def admin():
    form = AdminsPost()
    if form.validate_on_submit():
        Post.create_post(form.data)
    return render_template('admin/admin.html', form=form)


@admin_panel.route('/posts')
@admin_required
def posts():
    posts_view = db.session.query(Post).order_by(Post.id.desc()).all()
    return render_template('admin/posts.html', posts=posts_view)


@admin_panel.route('/users')
@admin_required
def users():
    users_views = db.session.query(Owner).order_by(Owner.id.desc()).all()
    return render_template('admin/users.html', users=users_views)


@admin_panel.route('/indicators')
@admin_required
def indicators():
    ind_views = db.session.query(Indicator).order_by(Indicator.month.desc()).all()
    return render_template('admin/indicators.html', indicators=ind_views)


@admin_panel.route('/post/<id>')
@admin_required
def posts(id):
    post = Post.query.get(id)
    return render_template('admin/post.html', post=post)


@admin_panel.route('/user/<id>')
@admin_required
def users(id):
    user = Owner.query.get(id)
    return render_template('admin/user.html', user=user)


@admin_panel.route('/indicator/<id>')
@admin_required
def indicators(id):
    indicator = Indicator.query.get(id)
    return render_template('admin/indicator.html', indicator=indicator)
