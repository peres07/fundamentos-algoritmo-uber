def quantidade_azulejos(comprimento: float, altura: float) -> int:
    '''Calcula a quantidade de azulejos inteiros necessários para preencher 
    uma parede com as dimensões informadas
    Exemplos:
    >>> quantidade_azulejos(6, 8)
    1200
    >>> quantidade_azulejos(6.5, 7)
    1138'''
    area_parede = comprimento * altura
    quantidade_azulejos = area_parede / 0.04
    if quantidade_azulejos / int(quantidade_azulejos) != 1:
        return int(quantidade_azulejos) + 1
    return int(quantidade_azulejos)
