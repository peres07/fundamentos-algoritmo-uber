from dataclasses import dataclass

@dataclass
class Aluno:
    ra: str
    nome: str
    curso: str

def main() -> None:
    '''Recebe o RA, nome e curso de um aluno e envia as informações para cadastro e, em seguida, imprime elas'''
    
    ra = input('Digite o RA do aluno: ')
    nome = input('Digite o nome do aluno: ')
    curso = input('Digite o curso do aluno: ')
    
    aluno = cadastrar_aluno(ra, nome, curso)

    imprimir_aluno(aluno)

def cadastrar_aluno(ra: str, nome: str, curso: str) -> Aluno:
    '''Recebe o RA, nome e curso de um aluno e o cadastra
    Exemplos: 
    >>> cadastrar_aluno('145095', 'José Luís', 'Ciencia da computacao')
    Aluno(ra='145095', nome='José Luís', curso='Ciencia da computacao')'''

    aluno = Aluno(ra, nome, curso)

    return aluno

def imprimir_aluno(aluno: Aluno) -> None:
    '''Recebe um aluno e imprime ele.'''
    print(f'RA do aluno: {aluno.ra}')
    print(f'Nome do aluno: {aluno.nome}')
    print(f'Curso do aluno: {aluno.curso}')

if __name__ == '__main__':
    main()
