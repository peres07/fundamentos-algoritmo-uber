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
    'VERMELHO'
    >>> cor_semaforo(Cor.VERMELHO).name
    'AMARELO'
    >>> cor_semaforo(Cor.AMARELO).name
    'VERDE'
    '''
    if cor == Cor.VERDE:
        return Cor.VERMELHO
    elif cor == Cor.VERMELHO:
        return Cor.AMARELO
    return Cor.VERDE
