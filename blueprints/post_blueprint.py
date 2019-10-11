from flask import Blueprint, redirect, render_template, request, url_for
from app import db
from classes.post import Post

bp = Blueprint('posts', __name__, url_prefix='/blog/post')

@bp.route('/add', methods=["GET", "POST"])
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


@bp.route('/edit/<int:id>', methods=["GET", "POST"])
def editPost(id):
    # Récupération du post
    post = Post.query.filter_by(id=id).first_or_404()# si jamais l'id n'existe pas

    if request.method == 'GET':
        return render_template('editPostForm.html', post=post)
    else:
        # Récupération de l'article
        post.update(request.form)

        return redirect(url_for('blog'))


@bp.route('/delete/<int:id>')
def deletePost(id):
    post = Post.query.filter_by(id=id).first_or_404()# si jamais l'id n'existe pas
    ##comment = Comment.query.filter_(post_id=id).all()
    db.session.execute("pragma foreign_keys=on ")# permet d'activer les clés étrangères
    db.session.delete(post)
    ##db.session.delete(comment)
    db.session.commit()
    return render_template('index.html')