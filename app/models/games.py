from . import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    console = db.Column(db.String(255))
    genre = db.Column(db.String(255))
