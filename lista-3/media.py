def media(media: float) -> str:
    '''Dado uma média de um aluno, retorne seu conceito:
    Exemplos:
    >>> media(1.2)
    'D'
    >>> media(6.1)
    'C'
    >>> media(8.4)
    'B'
    >>> media(9.6)
    'A'
    '''
    if 0 <= media <= 4.9:
        return "D"
    elif media <= 6.9:
        return "C"
    elif media <= 8.9:
        return "B"
    elif media <= 10:
        return "A"
    return "Média inválida"
