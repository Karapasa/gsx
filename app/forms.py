from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class Authorization(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Авторизоваться')


class FormSendMail(FlaskForm):
    from_whom = StringField('От кого(Имя/квартира)', validators=[DataRequired()])
    text = TextAreaField('Ваше сообщение', validators=[DataRequired()])
    submit = SubmitField('Отправить сообщение')


class Registration(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    apartment = IntegerField('Номер квартиры', validators=[DataRequired()])
    email = StringField('Ваш e-mail')
    phone_number = StringField('Ваш телефон')
    password = PasswordField('Введите пароль')
    submit = SubmitField('Зарегистрироваться')


class AdminsPost(FlaskForm):
    head = StringField('Заголовок', validators=[DataRequired()])
    posts_html = StringField('Объявление', validators=[DataRequired()])
    submit = SubmitField('Опубликовать объявление')


class SendIndicationWater(FlaskForm):
    cold_water = IntegerField('Холодная вода', validators=[DataRequired()])
    hot_water = IntegerField('Горячая вода', validators=[DataRequired()])
    submit = SubmitField('Отправить показания')


class SendEmail(FlaskForm):
    email = StringField('Ваш email: ', validators=[DataRequired()])
    text = StringField('Ваше сообщение: ', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Обновить пароль')
