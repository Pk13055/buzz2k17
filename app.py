from flask import Flask
from flask_cas import CAS
from flask_cas import login_required
from flask_cas import logout

app = Flask(__name__)
cas = CAS(app, '/cas')
app.config['CAS_SERVER'] = 'http://login.iiit.ac.in/'
app.config['SECRET_KEY'] = 'secret'


@app.route('/')
def route_index():
    return "Welcome"


@app.route('/login')
@login_required
def route_login():
    return "Welcome " + cas.username


@app.route('/logout')
def route_logout():
    return logout()


if __name__ == "__main__":
    app.run(port=3000)
