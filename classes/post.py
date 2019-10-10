from app import db
from datetime import datetime


class Post(db.Model):
    # colonne id en primary key, ce qui permet de l'incrémenter automatiquement
    id = db.Column(db.Integer, primary_key=True)
    # Colone name définit comme une chaine de caractère de longueur 80, ne peut pas être nul
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    comments = db.relationship('Comment', backref='Post', lazy=True)

    def update(self, values):
        self.title = values['postTitle']
        self.content = values['postContent']
        self.created_at = values['postCreatedAt']
        db.session.commit()