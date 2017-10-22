from flask import request, render_template, Blueprint, flash, redirect, url_for
from flask_cas import login_required
from time import time

from app import cas, db
from app.users.controllers import current_user
from app.users.models import User
from .models import Question

portal = 'gordian_knot'
mod_gnt = Blueprint(portal, __name__)


@mod_gnt.route('/', methods=['GET', 'POST'])
@login_required
def route_index():
    return redirect("http://bit.do/gordianknot")
    # u = current_user()
    # question = Question.query.get(u.gnt_q)
    # if question is None:
    #     flash('You have finished the quiz successfully! :D', 'alert-success')
    # score = u.gnt_s
    # if request.method == 'GET':
    #     return render_template('question.html', question=question, score=score,
    #                            portal=portal, user=u.email)
    # else:
    #     response = request.form['response']
    #     if response == question.answer:
    #         u.gnt_q += 1
    #         u.gnt_s += 100
    #         u.gnt_t = time()
    #         db.session.commit()
    #         flash('Your answer is correct!', 'alert-success')
    #     else:
    #         flash('Try again, your answer is incorrect :(', 'alert-danger')
    #     return redirect(url_for(portal+'.route_index'))


# @mod_lit.route('/leaderboard')
# @login_required
# def route_leaderboard():
#     u = current_user()
#     users = User.query.filter(User.gnt_t != 0)
#     s_users = sorted(users, key=lambda u: (u.gnt_s, -u.gnt_t), reverse=True)
#     u_users = [(u.email, u.gnt_s) for u in s_users]
#     return render_template('leaderboard.html', users=enumerate(u_users),
#                            portal=portal, user=u.email, score=u.gnt_s)
