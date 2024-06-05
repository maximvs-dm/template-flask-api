from models import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(9))


def teste(p):
    """ Resumo da função

    param: p
    return: None
    raises: 
        KeyError
    """

