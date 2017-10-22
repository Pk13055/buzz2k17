from app import db


class User(db.Model):

    __tablename__ = 'user'
    # Email ID
    email = db.Column(db.String(100), primary_key=True, nullable=False)
    # Lit Quiz
    lit_q = db.Column(db.INTEGER, default=1)
    lit_s = db.Column(db.INTEGER, default=0)
    lit_t = db.Column(db.REAL, default=0)
    # Cache-In
    cin_q = db.Column(db.INTEGER, default=1)
    cin_s = db.Column(db.INTEGER, default=0)
    cin_t = db.Column(db.REAL, default=0)
    # Hack-In
    hin_q = db.Column(db.INTEGER, default=1)
    hin_s = db.Column(db.INTEGER, default=0)
    hin_t = db.Column(db.REAL, default=0)
    # Gordian Knot
    gnt_q = db.Column(db.INTEGER, default=1)
    gnt_s = db.Column(db.INTEGER, default=0)
    gnt_t = db.Column(db.REAL, default=0)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return "<User %s>" % self.email
