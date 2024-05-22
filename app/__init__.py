import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.controller import bp_games

# Carrega variáveis de ambiente do arquivo `.env`
load_dotenv()


def create_app():
    """A criação da aplicação Flask é feita com o método fábrica
    """
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    # Inicializa as instâncias do SqlAlchemy e do Flask Migrate
    from app.model import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(bp_games)

    return app