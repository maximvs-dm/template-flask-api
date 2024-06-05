from flask import Blueprint, session

from app.services.viacep import get_address
from ..models.addresses import Address


bp_cadastro = Blueprint('cadastro', __name__)


@bp_cadastro.get('/')
def index():
    return "hello world!"


@bp_cadastro.get('/<int:cep>')
def add_address(cep):
    dados = get_address(cep)
    # salvo isso no banco

    print(dados)
    return dados

    result = open_wather_service.get_locale(name)