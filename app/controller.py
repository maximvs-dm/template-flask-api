from flask import Blueprint
from .model import Game


bp_games = Blueprint('games', __name__)


@bp_games.get('/')
def index():
    return "hello world!"
