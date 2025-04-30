def e_triangulo(x: float, y: float, z: float) -> bool:
    '''Dados 3 valores reais, determina se eles formam um triângulo
    >>> e_triangulo(16, 20, 30)
    True
    >>> e_triangulo(4, 7, 12)
    False'''
    if (x + y > z) and (x + z > y) and (z + y > x):
        return True
    return False

def tipo_triangulo(x: float, y: float, z: float) -> str:
    '''Dados 3 valores reais, determine se eles formam um triângulo e, se sim, qual o tipo de triângulo formado
    Exemplos:
    >>> tipo_triangulo(16, 20, 30)
    'Escaleno'
    >>> tipo_triangulo(15, 15, 15)
    'Equilátero'
    >>> tipo_triangulo(24, 24, 13)
    'Isósceles'
    >>> tipo_triangulo(4, 7, 12)
    'Não é um triângulo'
    '''
    if e_triangulo(x, y, z) == False:
        return 'Não é um triângulo'
    
    if (x == y) and (y == z):
        return 'Equilátero'
    elif (x == y) or (y == z) or (z == x):
        return 'Isósceles'
    else:
        return 'Escaleno'
