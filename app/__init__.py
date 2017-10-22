from flask import Flask
from flask_cas import CAS
from flaskext.csrf import csrf
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
csrf(app)
cas = CAS(app, '/cas')
db = SQLAlchemy(app)
app.config.from_object('config')

from app.users.controllers import mod_users
from app.portals.lit.controllers import mod_lit
from app.portals.cachein.controllers import mod_cin
from app.portals.gordianknot.controllers import mod_gnt

app.register_blueprint(mod_users)
app.register_blueprint(mod_lit, url_prefix='/lit')
app.register_blueprint(mod_cin, url_prefix='/cachein')
app.register_blueprint(mod_gnt, url_prefix='/gordianknot')

db.create_all()
