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


@app.route('/blog/post/edit/<id>', methods=["GET", "POST"])
def editPost(id):
    # Récupération du post
    post = Post.query.filter_by(id=id).first()

    if request.method == 'GET':
        return render_template('editPostForm.html', post=post)
    else:
        # Récupération de l'article
        post.update(request.form)

        return redirect(url_for('blog'))


@app.route('/blog/post/delete/<id>')
def deletePost(id):
    post = Post.query.filter_by(id=id).first()
    ##comment = Comment.query.filter_(post_id=id).all()
    db.session.delete(post)
    ##db.session.delete(comment)
    db.session.commit()
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
        comment = Comment(name=name, content=content, post_id=id)
        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('blog'))


@app.route('/blog/comment/edit/<id>', methods=["GET", "POST"])
def editComment(id):
    # Récupération du post
    comment = Comment.query.filter_by(id=id).first()

    if request.method == 'GET':
        return render_template('editMessageForm.html', comment=comment)
    else:
        # Récupération de l'article
        comment.update(request.form)

        return redirect(url_for('blog'))


@app.route('/blog/comment/delete/<id>')
def deleteComment(id):
    comment = Comment.query.filter_by(id=id).first()
    db.session.delete(comment)
    db.session.commit()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
