from app import db
from datetime import datetime

class Comment(db.Model):
    # colonne id en primary key, ce qui permet de l'incrémenter automatiquement
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    # Colone name définit comme une chaine de caractère de longueur 80, ne peut pas être nul
    name = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def update(self, form):
        self.name = form['messageName']
        self.content = form['messageContent']
        #self.created_at = datetime.utcnow() # pour mettre une nouvelle date à la modification
        db.session.commit()