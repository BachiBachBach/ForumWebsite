# Database models
from . import db
from flask_login import UserMixin
from datetime import datetime

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	data = db.Column(db.String(5000))
	date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User', backref='posts')


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(150), unique=True)
	password = db.Column(db.String(150))
	name = db.Column(db.String(150))