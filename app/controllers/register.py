from flask import Blueprint, request

bp_register = Blueprint('register', __name__, url_prefix='/cadastro')


@bp_register.get('/')
def index():
    return "hello world!"


@bp_register.post('/usuario')
def add_user():
    dados = request.json

    print(dados)
    return 'ok'
