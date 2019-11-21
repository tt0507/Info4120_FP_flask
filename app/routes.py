from flask import render_template, url_for, flash, redirect
from app import app
from app.model import User
from app.forms import LoginForm

@app.route('/')
def index():
	return render_template('index.html', title='Home')


@app.route('/about')
def about():
	return render_template('about.html', title='About')


@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.username.data == 'admin' and form.password.data == 'info4120':  # dummy login
			flash('Logged in', 'success')
			return redirect(url_for('index'))
		else:
			flash('Login unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)