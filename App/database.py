from App import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    middle_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    password_hash = db.Column(db.String(16), nullable=False)
