from flask import Flask
app = Flask(__name__)

# https://www.youtube.com/watch?v=MwZwr5Tvyxo

@app.route("/")
def hello():
	return "hello test"

@app.route("/about")
def about():
	return "about page"

if __name__ == '__main__':
    # allows you to dynamically update site like in angular
    app.debug = True
    # sets values
    app.run(host = '0.0.0.0', port = 5000)