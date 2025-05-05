def tempo_jogo(hora_inicio: int, minuto_inicio: int, hora_final: int, minuto_final: int) -> int:
    '''Recebe o horário que o jogo começou e o horário que o jogo terminou e retorna quanto tempo foram jogados em minutos
    Exemplos:
    >>> tempo_jogo(13, 40, 19, 20)
    400
    >>> tempo_jogo(12, 0, 19, 0)
    420
    >>> tempo_jogo(22, 0, 1, 0)
    180'''
    
    if 60 - minuto_inicio == 60:
        minutos_jogando = minuto_final
    else:
        minutos_jogando = (60 - minuto_inicio) + minuto_final

    if hora_inicio > hora_final:
        tempo_jogando = minutos_jogando + (((24 - hora_inicio) + (hora_final)) * 60) 
    else:
        tempo_jogando =  minutos_jogando + ((hora_final - hora_inicio) * 60)

    return tempo_jogando
