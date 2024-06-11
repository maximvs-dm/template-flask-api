from models import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(9))
    logradouro = db.Column(db.String(255))
    bairro = db.Column(db.String(255))
    cidade = db.Column(db.String(255))
    estado = db.Column(db.String(50))
