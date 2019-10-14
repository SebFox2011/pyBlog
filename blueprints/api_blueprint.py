from flask import Blueprint, redirect, render_template, request, url_for,jsonify
from classes.post import Post

bp_api = Blueprint('api', __name__, url_prefix='/api')

@bp_api.route('/posts')
def post_index ():
        postList = []
        posts = Post.query.all()

        for post in posts:
            postList.append(post.serialize())
        # show create form
        return jsonify(postList)