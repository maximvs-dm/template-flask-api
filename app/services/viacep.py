from requests import get


def get_address(cep):
    response = get(f'https://viacep.com.br/ws/{cep}/json/')
    return response.json()

class Viacep:
    def __init__(self, param):
        self.param = param
        self.key = 

    def get_address(self, bla):
        get(f'{self.param}/{bla}')

    def post_address(self, cep, data):
        pass