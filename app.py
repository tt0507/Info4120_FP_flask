from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return [User.username, User.password]


class Answer(db.Model):
	pass


class Log(db.Model):
	id = db.Column(db.Integer, primary_key=True)


class Question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	question = db.Column(db.String(20), unique=True, nullable=False)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/about')
def about():
	return render_template('about.html')


if __name__ == '__main__':
	app.run(debug=True)
