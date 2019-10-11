from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app import db

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

bp_auth.route('register')
def register ():
    return redirect(url_for('register'))

bp_auth.route('login')
def login ():
    return redirect(url_for('login'))

bp_auth.route('logout')
def logout ():
    return redirect(url_for('logout'))