# template-flask-api

Template para uma API Flask com SQLAlchemy e flask-migrate

## Como rodar o projeto

> Os comandos aqui são mostrados para a execução com o terminal do BASH (instalado com a instalação do git)

### Criação do ambiente virtual

VENV é um pacote padrão (já vem com a instalação do Python nas versões mais recentes)

1. Criar o ambiente virtual

```sh
venv <venv_name>
ou
py -m venv <venv_name>
```

2. Ativar o ambiente virtual

```sh
source ./<venv_name>/Scripts/Activate
```

### Instalação das dependencias/libs

```sh
pip install -r requirements.txt
```

### Inicializar/atualizar o banco de dados

```sh
flask db init       # rodar em um projeto novo
flask db migrate    # rodar ao baixar o projeto e sempre que houver alterações nas classes
flask db upgrade    # rodar para persistir as alteraçoes do comando anterior no banco
```

### Inicializar o servidor Flask

```sh
flask run
```

## Links para a documentação das libs usadas

- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Flask-SqlAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
