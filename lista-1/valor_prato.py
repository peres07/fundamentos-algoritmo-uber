def valor_prato(peso: float) -> float:
    '''Dado o peso de um prato em gramas, 
    calcula o valor final do prato baseado 
    no valor de R$50,00/kg
    Exemplos:
    >>> valor_prato(1500)
    75.0
    >>> valor_prato(750)
    37.5'''
    return (peso / 1000) * 50
