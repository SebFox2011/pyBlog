from app import db
from classes.post import Post
from datetime import datetime

class Comment(db.Model):
    # colonne id en primary key, ce qui permet de l'incrémenter automatiquement
    id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), primary_key=True)
    post = db.relationship('Post')
    # Colone name définit comme une chaine de caractère de longueur 80, ne peut pas être nul
    name = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def update(self, values):
        self.name = values['messageName']
        self.content = values['messageContent']
        self.created_at = values['messageCreatedAt']
        db.session.commit()