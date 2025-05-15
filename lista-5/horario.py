from dataclasses import dataclass

@dataclass
class Horario:
    horas: int
    minutos: int

def converter_horario(tempo_minutos: int) -> Horario:
    '''Recebe um tempo em minutos e retorna um horario do tipo *Horario*
    Exemplos: 
    >>> converter_horario(180)
    Horario(horas=3, minutos=0)
    >>> converter_horario(131)
    Horario(horas=2, minutos=11)'''

    horas = tempo_minutos // 60
    minutos = tempo_minutos % 60
    
    return Horario(horas, minutos)
