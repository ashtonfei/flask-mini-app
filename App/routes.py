from App import app, db
from flask import render_template, url_for, redirect
from App.database import User

from App.config import USER_HEADERS


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/users', methods=['GET', 'POST'])
def users():
    items = User.query.all()
    print(items)
    return render_template('users.html', items=items, headers=USER_HEADERS)


@app.route('/user/<id>', methods=['GET', 'POST'])
def user(id):
    user = User.query.filter_by(id=id).first()
    return render_template('user.html', user=user, headers=USER_HEADERS)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')


@app.route('/signout', methods=['GET', 'POST'])
def signout():
    return render_template('signout.html')
