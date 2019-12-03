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
    recent_answer = Answer.query.filter_by(user_id=1).order_by(Answer.id.desc()).first()
    past_answer = Answer.query.filter_by(user_id=1).order_by(Answer.id.desc()).all()

    return render_template('home.html', title='Home', recent_answer=recent_answer, past_answer=past_answer)


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


@app.route('/survey', methods=('POST', 'GET'))
def survey():
    form = Survey()
    # answer1 = form.question1.data
    if request.method == 'POST':
        answer1 = form.question1.data
        answer2 = form.question2.data
        answer3 = form.question3.data
        answer4 = form.question4.data
        return redirect(url_for('record', answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4))
    if not form.validate_on_submit():
        print('Form not validating')
    return render_template('survey.html', title='Survey', form=form)


@app.route('/record')
def record():
    answer1 = request.args.get('answer1')
    answer2 = request.args.get('answer2')
    answer3 = request.args.get('answer3')
    answer4 = request.args.get('answer4')

    log_data = Log(user_id=1)
    answer_data = Answer(user_id=1, log_number=1, question1=answer1, question2=answer2, question3=answer3,
                         question4=answer4)

    db.session.add(log_data)
    db.session.add(answer_data)
    db.session.commit()

    return render_template('record.html', title='Record')
