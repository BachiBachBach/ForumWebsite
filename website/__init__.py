from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


db = SQLAlchemy()

DB_NAME = 'database.db'


def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'NCUN*(N*#BCQ*B*CB#'
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	db.init_app(app)



	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(auth, url_prefix='/')

	from .models import User, Post

	create_database(app)

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))

	return app

def create_database(app):
	if not path.exists('/Users/harrisonbaker/Desktop/untitled folder/Teachpython/flaskProject/instance/' + DB_NAME):
		with app.app_context():
			db.create_all()
			print("Created Database!")