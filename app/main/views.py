from flask import render_template, current_app, redirect, url_for, flash
from flask_login import login_required, login_user, current_user, logout_user

from app import db
from . import main
from app.main.forms import Registration, Authorization, AdminsPost, SendEmail, ResetPasswordRequestForm, ResetPasswordForm
from app.models import Owner, reg_owner, create_post
from app.utils import send_mail, send_password_reset_email


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')


@main.route('/admin', methods=['GET', 'POST'])
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
        return redirect(url_for('.login'))


@main.route('/cabinet')
@main.route('/cabinet/<id>', methods=['GET', 'POST'])
@login_required
def cabinet(id):
    if current_user.is_authenticated:
        return render_template('cabinet.html', user_id=id)
    else:
        return redirect(url_for('.login'))


@main.route('/page')
def page():
    return render_template('page.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = Authorization()
    if form.validate_on_submit():
        user = db.session.query(Owner).filter(Owner.login == form.login.data).first()
        if user and user.check_password_hash(form.password.data):
            if user.role == 0:
                login_user(user, remember=False)
                return redirect(url_for('.cabinet', id=user.id))
            elif user.role == 1:
                login_user(user, remember=False)
                return redirect(url_for('.admin'))
    return render_template('login.html', form=form)


@main.route('/registration', methods=['GET', 'POST'])
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
            return redirect('.login')
        except:
            return 'Что-то пошло не так! Попробуйте еще раз'

    return render_template('registration.html', form=reg_form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))


@main.route('/send_message', methods=['GET', 'POST'])
def send_message():
    form = SendEmail()
    if form.validate_on_submit():
        email = form.email.data
        text = form.text.data
        text_msg = f'<p>Пользователь {email} пишет: <br><p>{text}</p>'
        recipients = ['alexmixpetrov@gmail.com']
        send_mail(recipients=recipients, text_msg=text_msg)
        flash('Письмо отправлено!')
        return redirect(url_for('.index'))
    return render_template('send_message.html', form=form)


@main.errorhandler(404)
def not_found_error(error):
    return render_template('page_404.html'), 404


@main.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = Owner.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Мы отправили Вам на почту инструкцию по смене пароля')
        return redirect(url_for('.login'))
    return render_template('reset_password_request.html', form=form)


@main.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('.index'))
    user = Owner.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Ваш пароль обновлен')
        return redirect(url_for('.login'))
    return render_template('reset_password.html', form=form)
