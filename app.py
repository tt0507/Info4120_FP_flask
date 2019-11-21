from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '91f605c898d3fe1082914c0e7dfda152'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.id}','{self.username}', '{self.password}')"


class Answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user = db.relationship('User', backref='user', lazy=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	log = db.relationship('Log', backref='log', lazy=True)
	log_number = db.Column(db.Integer, db.ForeignKey('log_number'), nullable=False)
	question1 = db.Column(db.String(20), unique=True, nullable=False)
	question2 = db.Column(db.String(20), unique=True, nullable=False)
	question3 = db.Column(db.String(20), unique=True, nullable=False)
	question4 = db.Column(db.String(20), unique=True, nullable=False)
	question5 = db.Column(db.String(20), unique=True, nullable=False)
	date_answer = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self, ):
		return f"User('{self.id}','{self.user_id}', '{self.log_numberd}', '{self.question1}', '{self.question2}', " \
		       f"'{self.question3}', '{self.question4}', '{self.question5}', '{self.date_answer}')"


class Log(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user = db.relationship('User', backref='user', lazy=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	log_number = db.Column(db.Integer)
	recent_sent_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"User('{self.id}','{self.user_id}', '{self.log_numberd}', '{self.recent_sent_date}')"


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


if __name__ == '__main__':
	app.run(debug=True)
