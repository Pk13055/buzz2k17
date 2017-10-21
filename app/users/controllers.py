from flask import request, render_template, Blueprint, redirect, url_for
from flask_cas import login_required, logout

from app import cas, db
from app.users.models import User


mod_users = Blueprint('users', __name__)


@mod_users.route('/ammap')
def route_ammap():
    return render_template('index.html')

@mod_users.route('/')
def route_index():
    if current_user() is None:
        return redirect(url_for('users.route_login'))
    return "Welcome " + current_user().email


@mod_users.route('/login')
@login_required
def route_login():
    u = db.session.query(User).get(cas.username)
    if u is None:
        db.session.add(User(cas.username))
        db.session.commit()
    return redirect(url_for('users.route_index'))


@mod_users.route('/logout')
def route_logout():
    return logout()


def current_user():
    if cas.username:
        return User.query.get(cas.username)
    else:
        return None
