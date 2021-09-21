from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Igor'}
    posts = [
        {
            'author': {'username': 'Igor'},
            'body': 'This is a test'
        },
        {
            'author': {'username': 'Flango'},
            'body': 'This is a test1'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)



