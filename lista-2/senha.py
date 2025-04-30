def senha(senha: str) -> bool:
    '''Faça um programa que lê uma senha e retorna se ela é a correta ou não
    Exemplos:
    >>> senha('teste')
    False
    >>> senha('senha')
    True'''
    if senha == 'senha':
        return True
    return False
