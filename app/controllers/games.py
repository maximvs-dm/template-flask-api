from flask import Blueprint

from app.services.viacep import get_address
from ..models.games import Game


bp_games = Blueprint('games', __name__)


@bp_games.get('/')
def index():
    return "hello world!"


@bp_games.get('/<int:cep>')
def teste_cep(cep):
    dados = get_address(cep)
    print(dados)
    return dados
