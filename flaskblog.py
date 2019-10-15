from flask import Flask,render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f9779cdd2a5db77c179c4174564e0a5f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # ref method so its capital
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # ref table name and field so its lower case
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    

messages = [
                {'author':'name',
                 'title':'filler title',
                 'content':'message',
                 'date_posted':'12-12-10'},
                
                {'author':'name',
                 'title':'filler title',
                 'content':'message',
                 'date_posted':'12-12-10'}
            ]


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', messages = messages)

@app.route("/about")
def about():
	return render_template("about.html", title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Signed up {form.username.data}', 'success')
        # name of method not mapping
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'pass':
            flash('logged in as admin', 'success')
            return redirect(url_for('home'))
        else:
            flash('Oops.. please check user credentials', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    # allows you to dynamically update site like in angular
    # sets values
    app.run(host = '0.0.0.0', port = 8080, debug = True)