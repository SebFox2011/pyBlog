from flask import Blueprint, redirect, render_template, request, url_for,session,g
from app import db
from classes.user import User

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

@bp_auth.route('/register', methods=['GET','POST'])
def register ():
    if request.method == 'GET':
        # show create form
        return render_template('register.html')
    else:
        # create post
        User.create(request.form)
        return redirect(url_for('auth.login'))


@bp_auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        # show create form
        return render_template('login.html')
    else:
        user = User.login(request.form)
        if user:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('blog'))
        else:
            return render_template('login.html', username=request.form["username"], password=request.form["password"])

@bp_auth.route('/logout', methods=["GET","POST"])
def logout ():
    session.clear()
    return redirect(url_for('index'))


@bp_auth.before_app_request
def load_logged_in_user():
    user_id=session.get('user_id')
    if user_id is None:
        g.user=None
    else:
        g.user=User.query.filter_by(id=user_id).first()