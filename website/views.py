from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import User, Post
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
	if request.method == 'POST':
		comment_text = request.form.get('post')
		if len(comment_text) < 1:
			flash("invalid comment", category='error')

		else:
			new_comment = Post(data=comment_text, user_id=current_user.id)
			db.session.add(new_comment)
			db.session.commit()
			flash("Successfuly added comment", category='success')

	comments = Post.query.all()
	return render_template('home.html', user=current_user, comments=comments)

@views.route('/delete-post', methods=['POST'])
def delete_post():
	post = json.loads(request.data)
	postId = post['postId']
	post = Post.query.get(postId)
	if post:
		if post.user_id == current_user.id:
			db.session.delete(post)
			db.session.commit()
			flash("Comment Deleted", category="success")

	return jsonify({})

