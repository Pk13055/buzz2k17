from app import db


class Question(db.Model):

    __tablename__ = 'hackin_question'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    body = db.Column(db.TEXT)
    answer = db.Column(db.String)

    def __init__(self, title, body, answer):
        self.title = title
        self.body = body
        self.answer = answer

    def __repr__(self):
        return "<Question %s>" % self.id
