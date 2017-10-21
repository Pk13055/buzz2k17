from flask import Flask
from flask_cas import CAS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
cas = CAS(app, '/cas')
db = SQLAlchemy(app)
app.config.from_object('config')

from app.users.controllers import mod_users
from app.portals.lit.controllers import mod_lit

app.register_blueprint(mod_users)
app.register_blueprint(mod_lit, url_prefix='/lit')

db.create_all()
