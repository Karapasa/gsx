from flask import render_template, redirect, url_for, flash
from flask_login import login_user, current_user

from app import db
from .forms import Registration, Authorization, ResetPasswordRequestForm, ResetPasswordForm
from app.models import Owner, reg_owner
from app.utils import send_password_reset_email
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = Authorization()
    if form.validate_on_submit():
        user = db.session.query(Owner).filter(Owner.login == form.login.data).first()
        if user and user.check_password_hash(form.password.data):
            if user.role == 0:
                login_user(user, remember=False)
                return redirect(url_for('main.cabinet', id=user.id))
            elif user.role == 1:
                login_user(user, remember=False)
                return redirect(url_for('main.admin'))
    return render_template('auth/login.html', form=form)


@auth.route('/registration', methods=['GET', 'POST'])
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
            return redirect(url_for('.login'))
        except:
            return 'Что-то пошло не так! Попробуйте еще раз'

    return render_template('auth/registration.html', form=reg_form)


@auth.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = Owner.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Мы отправили Вам на почту инструкцию по смене пароля')
        return redirect(url_for('.login'))
    return render_template('auth/reset_password_request.html', form=form)


@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = Owner.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Ваш пароль обновлен')
        return redirect(url_for('.login'))
    return render_template('auth/reset_password.html', form=form)
