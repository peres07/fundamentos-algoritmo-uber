def nivel(nivel: int, horas_jogadas: int) -> int:
    '''Recebe o nivel e a quantidade de horas jogadas e retorna o novo nível do jogador
    Exemplos:
    >>> nivel(3, 5)
    3
    >>> nivel(3, 8)
    6
    >>> nivel(3, 2)
    1
    '''
    if horas_jogadas < 4:
        novo_nivel = nivel - (4 - horas_jogadas)
    elif horas_jogadas <= 5:
        novo_nivel = nivel
    else:
        if horas_jogadas - 5 >= 7:
            novo_nivel = nivel + 7
        else:
            novo_nivel = nivel + (horas_jogadas - 5)

    if novo_nivel > 25:
        novo_nivel = 25
    if novo_nivel < 0:
        novo_nivel = 0

    return novo_nivel