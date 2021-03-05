from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class Registration(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    apartment = IntegerField('Номер квартиры', validators=[DataRequired()])
    email = StringField('Ваш e-mail')
    phone_number = StringField('Ваш телефон')
    password = PasswordField('Введите пароль')
    submit = SubmitField('Зарегистрироваться')


class Authorization(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Авторизоваться')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Обновить пароль')
