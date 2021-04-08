from App import app, db, login_manager
from flask import render_template, url_for, redirect, flash, request, abort
from flask_login import login_user
from App.database import User
from App.forms import LoginForm, RegisterForm

from App.config import USER_HEADERS, LOGIN_HEADERS, REGISTER_HEADERS


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id)


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=form.password.data,
            first_name=form.first_name.data,
            middle_name=form.middle_name.data,
            last_name=form.last_name.data,
            phone=form.phone.data,
            gender=form.gender.data)
        db.session.add(user)
        db.session.commit()

        flash(message='New user has been created successfully, you can now login to the system.', category='success')
        return redirect(url_for('login'))
    else:
        print(form.errors)
    return render_template('register.html', form=form, headers=REGISTER_HEADERS)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password_hash == password:
                login_user(user)
                flash(
                    message=f'Welcome, {user.first_name} {user.last_name}', category='success')
                # next = request.args.get('next')
                # if not is_safe_url(next):
                #     return abort(400)
                # return redirect(next or flask.url_for('home'))
            else:
                flash(
                    message=f'Wrong user or password, please try another one.', category='danger')
        else:
            flash(
                message=f'Wrong user or password, please try another one.', category='danger')
    else:
        print(form.errors)
    return render_template('login.html', form=form, headers=LOGIN_HEADERS)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('logout.html')
