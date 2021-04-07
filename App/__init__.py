from flask import Flask
from flask_bootstrap import Bootstrap

from flask_nav import Nav
from flask_nav.elements import *

from flask_sqlalchemy import SQLAlchemy

# app configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appdata.db'
app.config['SECRECT_KEY'] = 'fc436f88975911ebb0ec8cec4be902d0'

# apply bootstrap
Bootstrap(app)

# Nav bar
nav = Nav()
nav.register_element('top', Navbar('Mini App',
                                   View('Home', 'home'),
                                   View('Users', 'users'),
                                   View('About', 'about'),
                                   View('Sign In', 'signin'),
                                   View('Sign Out', 'signout'),
                                   View('Sign Up', 'signup')
                                   ))
nav.init_app(app)

# apply database
db = SQLAlchemy(app)
