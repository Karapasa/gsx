from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AdminsPost(FlaskForm):
    head = StringField('Заголовок', validators=[DataRequired()])
    posts_html = StringField('Объявление', validators=[DataRequired()])
    submit = SubmitField('Опубликовать объявление')
