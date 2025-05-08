from enum import Enum, auto
from dataclasses import dataclass

class Cor(Enum):
    VERDE = auto()
    AMARELO = auto()
    VERMELHO = auto()

def cor_semaforo(cor: Cor) -> Cor:
    '''Dada um cor atual de um semáforo, retorne a próxima cor
    Exemplos:
    >>> cor_semaforo(Cor.VERDE).name
    'AMARELO'
    >>> cor_semaforo(Cor.VERMELHO).name
    'VERDE'
    >>> cor_semaforo(Cor.AMARELO).name
    'VERMELHO'
    '''
    if cor == Cor.VERDE:
        return Cor.AMARELO
    elif cor == Cor.VERMELHO:
        return Cor.VERDE
    return Cor.VERMELHO
