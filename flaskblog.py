from flask import Flask
app = Flask(__name__)

# https://www.youtube.com/watch?v=MwZwr5Tvyxo

@app.route("/")
def hello():
	return "hello"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)