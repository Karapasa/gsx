from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user

from app.main.forms import SendEmail
from app.utils import send_mail
from . import main


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')


@main.route('/cabinet/<int:id>', methods=['GET', 'POST'])
@login_required
def cabinet(id):
    if current_user.is_authenticated:
        if id == int(current_user.get_id()):
            return render_template('cabinet.html', user_id=id)
        else:
            return f"ДОСТУП ЗАПРЕЩЕН!    ТЫ ЧЕГО СЕБЕ ПОЗВОЛЯЕШЬ?!    Я ЗНАЮ ТВОЙ IP! ЗА ТОБОЙ ВЫЕХАЛИ!"
    else:
        return redirect(url_for('auth.login'))


@main.route('/page')
def page():
    return render_template('page.html')


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
