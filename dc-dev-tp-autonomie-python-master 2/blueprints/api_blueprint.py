from flask import Blueprint, request, jsonify
from application import db
from models.post import Post

bp_api = Blueprint('api', __name__, url_prefix='/api')

@bp_api.route('/posts')
def post_index():
    posts = Post.query.all()
    postList = []
    for post in posts:
        print(post.serialize())
        postList.append(post.serialize())
    return jsonify(postList)
