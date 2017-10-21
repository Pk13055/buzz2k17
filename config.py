import os

CAS_SERVER = 'http://login.iiit.ac.in/'
SECRET_KEY = 'secret'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
