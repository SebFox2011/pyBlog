from flask import Blueprint, redirect, render_template, request, url_for
from app import db
from classes.comment import Comment

bp = Blueprint('comments', __name__, url_prefix='/blog/comment')

@bp.route('/add/<int:id>', methods=["GET", "POST"])
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


@bp.route('/edit/<int:id>', methods=["GET", "POST"])
def editComment(id):
    # Récupération du post
    comment = Comment.query.filter_by(id=id).first_or_404()# si jamais l'id n'existe pas

    if request.method == 'GET':
        return render_template('editMessageForm.html', comment=comment)
    else:
        # Récupération de l'article
        comment.update(request.form)

        return redirect(url_for('blog'))


@bp.route('/delete/<int:id>')
def deleteComment(id):
    comment = Comment.query.filter_by(id=id).first_or_404()# si jamais l'id n'existe pas
    db.session.delete(comment)
    db.session.commit()
    return render_template('index.html')