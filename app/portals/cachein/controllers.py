from flask import request, render_template, Blueprint, flash, redirect, url_for
from flask_cas import login_required
from time import time

from app import cas, db
from app.users.controllers import current_user
from app.users.models import User
from .models import Question

portal = 'cache_in'
mod_cin = Blueprint(portal, __name__)


@mod_cin.route('/', methods=['GET', 'POST'])
@login_required
def route_index():
    u = current_user()
    question = Question.query.get(u.cin_q)
    if question is None:
        flash('You have finished the quiz successfully! :D', 'alert-success')
    score = u.cin_s
    if request.method == 'GET':
        return render_template('question.html', question=question, score=score,
                               portal=portal, user=u.email)
    else:
        response = request.form['response']
        if response == question.answer:
            u.cin_q += 1
            u.cin_s += 100
            u.cin_t = time()
            db.session.commit()
            flash('Your answer is correct!', 'alert-success')
        else:
            flash('Try again, your answer is incorrect :(', 'alert-danger')
        return redirect(url_for('cache_in.route_index'))


@mod_cin.route('/leaderboard')
@login_required
def route_leaderboard():
    u = current_user()
    users = User.query.filter(User.cin_t != 0)
    s_users = sorted(users, key=lambda u: (u.cin_s, -u.cin_t), reverse=True)
    u_users = [(u.email, u.cin_s) for u in s_users]
    return render_template('leaderboard.html', users=enumerate(u_users),
                           portal=portal, user=u.email, score=u.cin_s)
