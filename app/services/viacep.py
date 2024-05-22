from requests import get


def get_address(cep):
    response = get(f'https://viacep.com.br/ws/{cep}/json/')
    return response.json()
