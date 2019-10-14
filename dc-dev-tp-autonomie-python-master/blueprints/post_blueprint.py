from flask import Blueprint, redirect, render_template, request, url_for
from application import db
from models.post import Post

bp_post = Blueprint('posts', __name__, url_prefix='/posts')

@bp_post.route('/')
def post_index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@bp_post.route('/create')
def create_post():
    return render_template('create_post.html')

@bp_post.route('/', methods=['POST'])
def store_post():
    Post.create(request.form)
    return redirect(url_for('posts.post_index'))

@bp_post.route('/<int:post_id>')
def show_post(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    return render_template('show_post.html', post=post)

@bp_post.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    if request.method == 'GET':
        return render_template('edit_post.html', post=post)
    else:
        post.update(request.form)
        return redirect(url_for('posts.show_post', post_id=post.id))