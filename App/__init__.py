
from flask import Flask
from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# app configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appdata.db'
app.config['SECRET_KEY'] = 'fc436f88975911ebb0ec8cec4be902d0'

# apply bootstrap
Bootstrap(app)

# apply database
db = SQLAlchemy(app)

# apply login manager
login_manager = LoginManager()
login_manager.init_app(app)
