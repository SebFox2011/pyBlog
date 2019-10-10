from post import Post

post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), primary_key=True)
post = db.relationship('Post')