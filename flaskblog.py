from flask import Flask
from flask import render_template
import os
app = Flask(__name__)


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

if __name__ == "__main__":
    # allows you to dynamically update site like in angular
    # sets values
    app.run(host = '0.0.0.0', port = 8080, debug = True)