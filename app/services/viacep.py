from requests import get
import re

cep_pattern = re.compile(r'^\d{2}\.?\d{3}-?\d{3}$', re.IGNORECASE | re.MULTILINE)
not_number_pattern = re.compile(r'\D')


def get_address(cep):
    if not cep_pattern.match(cep):
        raise Exception(f'Cep com formato inválido: {cep}')

    cep_numbers = not_number_pattern.sub('', cep)

    response = get(f'https://viacep.com.br/ws/{cep_numbers}/json/')
    return response.json()
