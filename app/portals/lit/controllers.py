from flask import request, render_template, Blueprint
from flask_cas import login_required

from app import cas, db
from app.users.controllers import current_user
from app.users.models import User
from .models import Question


mod_lit = Blueprint('lit', __name__)

portal = 'Lit'


@mod_lit.route('/', methods=['GET', 'POST'])
@login_required
def route_index():
    u = current_user()
    question = Question.query.get(u.lit_q)
    score = u.lit_s
    if request.method == 'GET':
        return render_template('question.html', question=question, score=score,
                               portal=portal)
    else:
        response = request.form['response']
        if response == question.answer:
            u.lit_q += 1
            u.lit_s += 100
            db.session.commit()
            return 'Your answer is correct!!!'
        else:
            return 'Try again!!! :('


@mod_lit.route('/leaderboard')
def route_leaderboard():
    users = User.query.all()
    sorted_users = sorted(users, key=lambda u: (u.lit_s, -u.lit_t))
    return render_template('leaderboard.html', users=sorted_users, portal=portal)
