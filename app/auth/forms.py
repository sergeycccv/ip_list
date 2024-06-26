from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired('Введите имя пользователя')])
    password = PasswordField('Пароль', validators=[DataRequired('Введите пароль')])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')


class RegistrationForm(FlaskForm):
    username = StringField('Пользователь', validators=[DataRequired('Введите имя пользователя')])
    email = StringField('Email', validators=[DataRequired('Введите email'), Email('Некорректный email')])
    password = PasswordField('Пароль', validators=[DataRequired('Придумайте пароль')])
    password2 = PasswordField('Подтверждение пароля', \
                              validators=[DataRequired('Введите пароль еще раз'), EqualTo('password', message='Пароли не совпадают')])
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


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Введите email'), Email('Некорректная почта')])
    submit = SubmitField('Сбросить пароль')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Пароль', validators=[DataRequired('Введите пароль')])
    password2 = PasswordField(
        'Повторите пароль', validators=[DataRequired('Введите пароль ещё раз'), EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Сохранить')
