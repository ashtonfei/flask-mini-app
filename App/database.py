from App import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    middle_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False, unique=True)
    gender = db.Column(db.String(10), nullable=False)
    password_hash = db.Column(db.String(16), nullable=False)


def __repr__(self):
    return '<User %r>' % self.username
