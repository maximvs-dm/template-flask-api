import os
from dotenv import load_dotenv
from flask import Flask
from app.controllers.games import bp_games

# Carrega variáveis de ambiente do arquivo `.env`
load_dotenv()


def create_app():
    """Criação da aplicação Flask 

    A aplicação é criada com o método fábrica
    e uso de blueprints (por hora só tem uma)
    """
    app = Flask(__name__)

    # adiciona a configuração com o enderço do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    # Inicializa as instâncias do SqlAlchemy e do Flask Migrate
    from app.models.games import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # registra a(s) blueprint(s)
    app.register_blueprint(bp_games)

    return app
