from application import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    comments = db.relationship('Comment', backref='post', passive_deletes=True)

    @classmethod
    def create(cls, form):
        postTitle = form['title']
        postBody = form['body']
        post = Post(title=postTitle, body=postBody)
        db.session.add(post)
        db.session.commit()
        return post
    
    def update(self, form):
        self.title = form['title']
        self.body = form['body']
        db.session.commit()

    def serialize(self):
        commentList = []
        for comment in self.comments:
            commentList.append(comment.serialize())
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at.strftime('%d/%m/%Y'),
            'comments': commentList
        }