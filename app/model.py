from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
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
    log_number = db.Column(db.Integer, db.ForeignKey('log.id'), nullable=False)
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
    user = db.relationship('User', backref='user_id', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    log_number = db.Column(db.Integer)
    recent_sent_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.id}','{self.user_id}', '{self.log_numberd}', '{self.recent_sent_date}')"
