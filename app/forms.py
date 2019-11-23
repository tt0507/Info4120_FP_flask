from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from app.model import User


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

	def valiate_username_password(self, username, password):
		user = User.query.filter_by(username=username.data).first()
		password = User.query.filter_by(password=password.data).first()

		if username.data != user:
			raise ValidationError('Wrong Username')


class Survey(FlaskForm):
	question1 = SelectField('How are you feeling right now?', choices=[(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
	                                                                    ('5', '5'))], validators=[DataRequired()])
	question2 = SelectField('What were you doing at the moment the survey was sent?',
	                        choices=[(('sports', 'Sports'), ('study', 'Study'), ('rest', 'Resting'),
	                                  ('eating', 'Eating'), ('others', 'Others'))], validators=[DataRequired()])
	question3 = SelectField('Are you feeling sad right now?', choices=[(('no', 'No'), ('yes', 'Yes'))], validators=[DataRequired()])
	question4 = SelectField('Do you feel worse than yesterday?',
	                        choices=[(('no', 'No'), ('yes', 'Yes'))], validators=[DataRequired()])
	submit = SubmitField('Submit')
