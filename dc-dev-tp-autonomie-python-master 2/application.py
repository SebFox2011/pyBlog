from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'clésecrète'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.post import Post
from models.comment import Comment
from models.user import User
from blueprints.post_blueprint import bp_post
from blueprints.comment_blueprint import bp_comment
from blueprints.auth_blueprint import bp_auth
from blueprints.api_blueprint import bp_api
import doc

app.register_blueprint(bp_post)
app.register_blueprint(bp_comment)
app.register_blueprint(bp_auth)
app.register_blueprint(bp_api)

@app.route('/')
def index():
    return redirect(url_for('posts.post_index'))

