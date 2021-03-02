from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class FormSendMail(FlaskForm):
    from_whom = StringField('От кого(Имя/квартира)', validators=[DataRequired()])
    text = TextAreaField('Ваше сообщение', validators=[DataRequired()])
    submit = SubmitField('Отправить сообщение')


class SendIndicationWater(FlaskForm):
    cold_water = IntegerField('Холодная вода', validators=[DataRequired()])
    hot_water = IntegerField('Горячая вода', validators=[DataRequired()])
    submit = SubmitField('Отправить показания')


class SendEmail(FlaskForm):
    email = StringField('Ваш email: ', validators=[DataRequired()])
    text = TextAreaField('Ваше сообщение: ', validators=[DataRequired()])
    submit = SubmitField('Отправить')
