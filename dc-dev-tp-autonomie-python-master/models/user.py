from application import db
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    @classmethod
    def create(cls, form):
        username = form['username']
        password = form['password']
        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def login(cls, form):
        username = form['username']
        password = form['password']
        user = User.query.filter_by(username=username).first()
        if user is None:
            return None
        elif check_password_hash(user.password, password):
            return user
        else: 
            return None