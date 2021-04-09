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


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)

    modified_on = db.Column(db.DateTime)
    modified_by = db.Column(db.Integer)

    part_number = db.Column(db.String(18), nullable=False, unique=True)
    description = db.Column(db.String(60), nullable=False, unique=True)
    vendors = db.Column(db.Integer)
    price = db.Column(db.Float, default=0)
    sell_price = db.Column(db.Float, default=0)
    stock = db.Column(db.Integer, default=0)
