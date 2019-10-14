from flask import Flask,render_template, url_for
from forms import RegistrationForm, LoginForm
import os
app = Flask(__name__)

app.config['SECRET'] = 'f9779cdd2a5db77c179c4174564e0a5f'

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
def hello():
	return render_template('home.html', messages = messages)

@app.route("/about")
def about():
	return render_template("about.html", title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)
'''
@app.route("/login")
def login():
    login = LoginForm()
    return render_template('login.html', title='Register', form=form)'''

if __name__ == "__main__":
    # allows you to dynamically update site like in angular
    # sets values
    app.run(host = '0.0.0.0', port = 8080, debug = True)