from flask import Flask
from flask import render_template  # jinja2
from flask import request
from flask import redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

###api
import requests,json

app = Flask(__name__)
app.secret_key = 'clésecrete' # clé secrete pour la sessions
## création de la base données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

##pour flask-migrate
migrate = Migrate(app, db)

from classes.post import Post
from classes.comment import Comment
from classes.user import User
from blueprints.post_blueprint import bp_post
from blueprints.comment_blueprint import bp_comment
from blueprints.auth_blueprint import bp_auth
from blueprints.api_blueprint import bp_api

# enregistre les blueprint route dans add
app.register_blueprint(bp_post)
app.register_blueprint(bp_comment)
app.register_blueprint(bp_auth)
app.register_blueprint(bp_api)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    posts = Post.query.all()
    comments = Comment.query.all()
    return render_template('blog.html', posts=posts, comments=comments)


@app.route('/test')
def test():
    url=[]
    response = requests.get('https://api.unsplash.com/photos/random?client_id=9838ead1b3ff626e5c216427d4d41cbef2344367ddc7cde9a1e04c13f2efbcb1')
    content = json.loads(response.text) # retourne un dictionnaire
    url = content['urls']['raw']
    #for item in content:
    #    url.append(item.urls.raw)
    return redirect(url)

if __name__ == '__main__':
    app.run()
