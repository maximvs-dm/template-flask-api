from . import db

addresses = db.Table(
    'addresses',
    db.Column('user_id', db.Integer, db.ForeignKey('address.id'), primary_key=True),
    db.Column('address_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

games = db.Table(
    'addresses',
    db.Column('user_id', db.Integer, db.ForeignKey('address.id'), primary_key=True),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    address = db.relationship('Address', secondary=addresses, lazy='subquery',
                              backref=db.backref('users', lazy=True))
    games = db.relationship('Game', secondary=games, lazy='subquery',
                            backref=db.backref('users', lazy=True))
