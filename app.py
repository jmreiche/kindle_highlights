from crypt import methods
from unicodedata import name
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	title = "Kindle Highlights"
	return render_template('index.html', title = title)

@app.route('/dashboard/<name>')
def dashboard(name):
	return "Hello " + name

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		user = request.form['name']
		return redirect(url_for('dashboard', name = user))
	else:
		user = request.args.get('name')
		return render_template('login.html')


if __name__ == '__main__':
	app.run(debug=True)