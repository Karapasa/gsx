from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AdminsPost(FlaskForm):
    tag = StringField('Тип страницы', validators=[DataRequired()])
    header = StringField('Заголовок', validators=[DataRequired()])
    url = StringField('URl страницы')
    cardtext = StringField('Превью страницы', validators=[DataRequired()])
    htmltext = StringField('Html текст страницы')
    # submit = SubmitField('Опубликовать объявление')
