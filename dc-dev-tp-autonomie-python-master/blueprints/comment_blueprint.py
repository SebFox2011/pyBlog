from flask import Blueprint, redirect, render_template, request, url_for
from application import db
from models.comment import Comment

bp_comment = Blueprint('comments', __name__, url_prefix='/comments')

@bp_comment.route('/', methods=['POST'])
def store_comment():
    comment = Comment.create(request.form)
    return redirect(url_for('posts.show_post', post_id=comment.post_id))