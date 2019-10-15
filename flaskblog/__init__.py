from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskbcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f9779cdd2a5db77c179c4174564e0a5f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes