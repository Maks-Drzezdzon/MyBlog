from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__) # setup for flask

app.config['SECRET_KEY'] = 'f9779cdd2a5db77c179c4174564e0a5f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app) # handles db operations
bcrypt = Bcrypt(app) # handles pass encrypt
login_manager = LoginManager(app) # handles sessions


from flaskblog import routes