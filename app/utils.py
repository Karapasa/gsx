from threading import Thread

from flask import make_response, render_template
from flask_mail import Message

from app import app, db
from app.models import Owner


def cookies():
    res = make_response("")
    user_id = db.session.query(Owner).get(int(id))
    res.set_cookie("id", user_id, 60 * 60 * 24 * 15)


def async_send_mail(app, msg):
    with app.app_context():
        send_mail(msg)


def send_mail(subject, sender, recipients, text, html):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text
    msg.html = html
    thr = Thread(target=async_send_mail, args=[app, msg])
    return thr


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail('[GSH] Обновление вашего пароля',
              sender=app.config['ADMINS'][0],
              recipients=[user.email],
              text_body=render_template('email/reset_password.txt',
                                        user=user, token=token),
              html_body=render_template('email/reset_password.html',
                                        user=user, token=token))
