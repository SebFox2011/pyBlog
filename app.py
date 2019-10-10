from flask import Flask
from flask import render_template  # jinja2
from flask import request
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
## création de la base données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

##pour flask-migrate
migrate = Migrate(app, db)

from classes.post import Post
from classes.comment import Comment


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    posts = Post.query.all()
    comments = Comment.query.all()
    return render_template('blog.html', posts=posts, comments=comments)
    #return render_template('blog.html')

@app.route('/blog/post/add', methods=["GET", "POST"])
def addPost():
    if request.method == 'GET':
        # show create form
        return render_template('addPostForm.html')
    else:
        # create post
        title = request.form['postTitle']
        content = request.form['postContent']
        # Création du post
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('blog'))


@app.route('/blog/post/edit')
def editPost():
    return render_template('index.html')


@app.route('/blog/post/delete')
def deletePost():
    return render_template('index.html')


@app.route('/blog/comment/add/<id>', methods=["GET", "POST"])
def addComment(id):
    if request.method == 'GET':
        # show create form
        return render_template('addMessageForm.html')
    else:
        # create post
        name = request.form['messageName']
        content = request.form['messageContent']
        # Création du post
        comment = Comment(name=name, content=content,post_id=id)
        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('blog'))


@app.route('/blog/comment/edit')
def editComment():
    return render_template('index.html')


@app.route('/blog/comment/delete')
def deleteComment():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
