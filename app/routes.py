from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
#@app.route('/index')
def index():
    user = {'username': 'Сергей'}
    posts = [
        {
        'author': {'username': 'Алексей'},
        'body': 'Это сообщение от Алексей!'
        },
        {
        'author': {'username': 'Дарья'},
        'body': 'А это сообщение от Дарьи!'
        }
    ]
    return render_template('index.html', title='Главная страница', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Пользователь {form.username.data} успешно зашёл, remember_me = {form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Вход в систему', form=form)
