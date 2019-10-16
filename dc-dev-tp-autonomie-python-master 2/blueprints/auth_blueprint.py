from flask import Blueprint, redirect, render_template, request, url_for, session, g
from application import db
from models.user import User

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

#route register
@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        User.create(request.form)
        return redirect(url_for('auth.login'))
    else:
        return render_template('register.html')

#route login
@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.login(request.form)
        if user:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('posts.post_index'))
        else:
            return render_template('login.html', error='Login et/ou mot de passe incorrect',username=request.form["username"], password=request.form["password"])
    else:
        return render_template('login.html')

@bp_auth.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('posts.post_index'))

@bp_auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()
