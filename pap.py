from flask import Flask 
from flask import render_template
from flask import redirect

app = Flask(__name__)

@app.route("/")
def hello():
	#name = "bilal"
	return render_template("index.html")

@app.route("/world")
def world():
	return "world"

if __name__ == '__main__':
	app.run(debug=True)