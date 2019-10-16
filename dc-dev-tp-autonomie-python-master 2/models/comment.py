from application import db
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    author_name = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @classmethod
    def create(cls, form):
        commentAuthor = form['author']
        commentContent = form['content']
        commentPostId = form['post_id']
        comment = Comment(post_id=commentPostId, author_name=commentAuthor, content=commentContent)
        db.session.add(comment)
        db.session.commit()
        return comment

    def serialize(self):
        return {
            'id': self.id,
            'author': self.author_name,
            'content': self.content,
            'created_at': self.created_at.strftime('%d/%m/%Y')
        }