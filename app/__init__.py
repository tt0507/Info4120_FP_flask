from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from fitbit import Fitbit

app = Flask(__name__)
app.config['SECRET_KEY'] = '91f605c898d3fe1082914c0e7dfda152'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
fitbit = Fitbit(client_id='22BFHK', client_secret='92af1fb017e08d1b4426a5e092257e85')

from app import routes
