from app import db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @classmethod
    def create(cls,form):
        username = form['username']
        password = form['pwd1']
        user = User(username=username,password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def login(cls,form):
        username = form['username']
        password = form['password']
        user = User.query.filter_by(username=username).first()
        if username is None:
            return None
        elif check_password_hash(user.password, password):
            return user
        else:
            return None

