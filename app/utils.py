import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Thread

from flask import make_response, current_app

from app import db
from app.models import Owner


def cookies():
    res = make_response("")
    user_id = db.session.query(Owner).get(int(id))
    res.set_cookie("id", user_id, 60 * 60 * 24 * 15)


def async_send_mail(sender, recipients, msg):
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(current_app.config['MAIL_DEFAULT_SENDER'], current_app.config['MAIL_PASSWORD'])
    server.sendmail(sender, recipients, msg.as_bytes())
    server.quit()


def send_mail(subject='Письмо от администрации Flask-GSX', sender='alexmixpetrov@yandex.ru', recipients=[],
              text_msg=""):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients[0]
    text = f'<html><head></head><body><h2>Добрый день!</h2><div>{text_msg}</div></body></html>'
    html_text = MIMEText(text, 'html')
    msg.attach(html_text)
    Thread(target=async_send_mail, args=[sender, recipients, msg]).start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail(subject='[GSH] Обновление вашего пароля',
              recipients=[user.email],
              text_msg=f'<p>Чтобы сбросить пароль пройдите по <a href=http://127.0.0.1:5000/reset_password/{token}>ссылке</a></p>')