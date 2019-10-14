from app import db
from datetime import datetime
from classes.comment import Comment
from flask import jsonify


class Post(db.Model):
    # colonne id en primary key, ce qui permet de l'incrémenter automatiquement
    id = db.Column(db.Integer, primary_key=True)
    # Colone name définit comme une chaine de caractère de longueur 80, ne peut pas être nul
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    #content = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    comments = db.relationship(Comment, backref='Post', lazy=True,passive_deletes=True)

    def update(self, form):
        self.title = form['postTitle']
        self.content = form['postContent']
        #self.created_at = datetime.utcnow() # pour mettre une nouvelle date à la modification
        db.session.commit()

    def serialize (self):
        commentList = []
        comments = Comment.query.all()

        for comment in comments:
            commentList.append(comment.serialize())
        # création d'un dictionnaire pour l'objet
        return {
            'id':self.id,
            'title':self.title,
            'content':self.content,
            'comments':commentList,
            'created_at':self.created_at.strftime('%d/%m/%Y')
        }
