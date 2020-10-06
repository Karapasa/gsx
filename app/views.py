from app import app, db
from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user
from app.forms import Registration, Authorization, AdminsPost
from app.models import Owner, reg_owner, create_post
from app.utils import cookies


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    form = AdminsPost()
    if form.validate_on_submit():
        header = form.head.data
        htmltext = form.posts_html.data
        create_post(header, htmltext)
    if current_user.is_authenticated and db.session.query(Owner).filter(Owner.role == 1).first():
        return render_template('admin.html', form=form)
    else:
        return redirect(url_for('login'))


@app.route('/cabinet/<id>', methods=['GET', 'POST'])
@login_required
def cabinet(id):
    if current_user.is_authenticated:
        return render_template('cabinet.html', user_id=id)
    else:
        return redirect(url_for('login'))


@app.route('/page')
def page():
    return render_template('page.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Authorization()
    if form.validate_on_submit():
        user = db.session.query(Owner).filter(Owner.login == form.login.data).first()
        if user and user.check_password_hash(form.password.data):
            if user.role == 0:
                login_user(user, remember=False)
                return redirect(url_for('cabinet', id=user.id))
            elif user.role == 1:
                login_user(user, remember=False)
                return redirect(url_for('admin'))
    return render_template('login.html', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def regist():
    reg_form = Registration()
    if reg_form.validate_on_submit():
        login = reg_form.login.data
        apartment = reg_form.apartment.data
        email = reg_form.email.data
        phone_number = reg_form.phone_number.data
        password = reg_form.password.data
        try:
            reg_owner(login=login, email=email, phone_number=phone_number, apartment=apartment, password=password)
            return redirect('login')
        except:
            return 'Что-то пошло не так! Попробуйте еще раз'

    return render_template('registration.html', form=reg_form)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found_error(error):
    return render_template('page_404.html'), 404
