from flask import make_response
from app import app, db
from app.models import Owner
from threading import Thread
from flask_mail import Message


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
