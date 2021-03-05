from app import db
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user
from app.main.forms import SendEmail, SendIndicationWater
from app.models import Post, Owner, Indicator
from app.utils import send_mail
from . import main


@main.route('/')
@main.route('/index')
def index():
    post = db.session.query(Post).order_by(Post.id.desc()).all()
    return render_template('index.html', user=current_user, posts=post)


@main.route('/cabinet/<int:id>', methods=['GET', 'POST'])
@login_required
def cabinet(id):
    if current_user.is_authenticated:
        if id == int(current_user.get_id()):
            cur_user = Owner.query.get(id)
            indicators = cur_user.indicators
            form = SendIndicationWater()
            if form.validate_on_submit():
                datas = form.data
                Indicator.save_indications(datas, id)
                return redirect(url_for('main.cabinet', id=id))
            return render_template('cabinet.html', cur_user=cur_user, user=current_user, form=form, indicators=indicators)
        else:
            return f"ДОСТУП ЗАПРЕЩЕН!    ТЫ ЧЕГО СЕБЕ ПОЗВОЛЯЕШЬ?!    Я ЗНАЮ ТВОЙ IP! ЗА ТОБОЙ ВЫЕХАЛИ!"
    else:
        return redirect(url_for('auth.login'))


@main.route('/page/<url>')
def page(url):
    post = Post.query.filter_by(url=url).first()
    return render_template('page.html', user=current_user, post=post, title=post.header)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))


@main.route('/send_message', methods=['GET', 'POST'])
@login_required
def send_message():
    form = SendEmail()
    user_email = Owner.query.filter_by(id=int(current_user.get_id())).first()
    if form.validate_on_submit():
        email = form.email.data
        text = form.text.data
        text_msg = f'<p>Пользователь {email} пишет: <br><p>{text}</p>'
        recipients = ['alexmixpetrov@gmail.com']
        send_mail(recipients=recipients, text_msg=text_msg)
        flash('Письмо отправлено!')
        return redirect(url_for('.index'))
    return render_template('send_message.html', form=form, user_email=user_email.email)
