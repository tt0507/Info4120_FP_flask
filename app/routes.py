from flask import render_template, url_for, flash, redirect, request, json, session
from app import app, db, bcrypt
from app.model import User, Log, Answer
from app.forms import LoginForm, Survey
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def index():
	return render_template('index.html', title='Home')


@app.route('/about')
def about():
	return render_template('about.html', title='About')


@app.route('/home')
def home():
	return render_template('home.html', title='Home')


@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and (user.password == form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next) if next_page else redirect(url_for('home'))
		else:
			flash('Login unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


@app.route('/log')
@login_required
def log():
	return render_template('log.html', title='Log')


@app.route('/survey', methods=['POST', 'GET'])
def survey():
	form = Survey()
	# if request.method == 'POST':
	if form.validate_on_submit():
		answer1 = request.form.get('question1')
		answer2 = request.form.get('question2')
		answer3 = request.form.get('question3')
		answer4 = request.form.get('question4')
		return redirect(url_for('record'))
	return render_template('survey.html', title='Survey', form=form)


@app.route('/record')
def record():
	return render_template('record.html', title='Record')
