from enum import Enum, auto
from dataclasses import dataclass

class Tamanho(Enum):
    CURTO = auto()
    LONGO = auto()
    MEDIANO = auto()

def tamanho_nome(nome: str) -> Tamanho:
    '''Dado um nome, retorne o tamanho dele (curto, mediano ou longo)
    Exemplos:
    >>> tamanho_nome('Isabella').name
    'MEDIANO'
    >>> tamanho_nome('Alexandra').name
    'LONGO'
    >>> tamanho_nome('José').name
    'CURTO'
    '''
    if len(nome) <= 4:
        return Tamanho.CURTO
    elif len(nome) <= 8:
        return Tamanho.MEDIANO
    return Tamanho.LONGO
