from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired('Введите имя пользователя')])
    password = PasswordField('Пароль', validators=[DataRequired('Введите пароль')])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')


class RegistrationForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired()])
    email = StringField('Почта', validators=[DataRequired(), Email('Некорректная почта')])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Подтверждение пароля', \
                              validators=[DataRequired(), EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Пожалуйста, используйте другое имя пользователя')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Пожалуйста, используйте другой адрес электронной почты')


class EditProfileForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired()])
    about_me = TextAreaField('Обо мне', validators=[Length(min=0, max=140)])
    submit = SubmitField('Сохранить')

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(
                User.username == self.username.data))
            if user is not None:
                raise ValidationError('Это имя пользователя уже занято')


# Форма для подписки и отмены подписки
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')