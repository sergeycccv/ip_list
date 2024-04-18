from flask import render_template
from app import app
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
