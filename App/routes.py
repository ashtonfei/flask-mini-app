from App import app, db, login_manager
from flask import render_template, url_for, redirect, flash, request, abort
from flask_login import login_user, logout_user, current_user, login_required

from App.database import User
from App.forms import LoginForm, RegisterForm

from App.config import USER_HEADERS, LOGIN_HEADERS, REGISTER_HEADERS


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def home():
    print(current_user)
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('home.html', current_user=current_user)


@app.route('/about', methods=['GET', 'POST'])
@login_required
def about():
    return render_template('about.html', current_user=current_user)


@app.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    items = User.query.all()
    return render_template('users.html', current_user=current_user, items=items, headers=USER_HEADERS)


@app.route('/users/<id>', methods=['GET', 'POST'])
@login_required
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

        flash(message='New user has been created successfully, you can now login to the system.', category='warning')
        return redirect(url_for('login'))
    else:
        pass
    return render_template('register.html', current_user=current_user, form=form, headers=REGISTER_HEADERS)


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
                print(current_user)
                flash(
                    message=f'Welcome, {user.first_name} {user.last_name}', category='warning')
                return redirect(url_for('home'))
            else:
                flash(
                    message=f'Wrong user or password, please try another one.', category='danger')
        else:
            flash(
                message=f'Wrong user or password, please try another one.', category='danger')
    else:
        print(form.errors)
        pass
    return render_template('login.html', current_user=current_user, form=form, headers=LOGIN_HEADERS)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
