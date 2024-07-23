"""
Exercício 04 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    >>> vogal_ou_consoante("F")
    'consoante'
    >>> vogal_ou_consoante("a")
    'vogal'
    >>> vogal_ou_consoante('c')
    'consoante'
    >>> vogal_ou_consoante('U')
    'vogal'
"""


def vogal_ou_consoante(letra):
    """Escreva aqui em baixo a sua solução"""

    vogais = {
        'a': 'A',
        'e': 'E',
        'i': 'I',
        'o': 'O',
        'u': 'U'
    }

    if letra in vogais.keys() or letra in vogais.values():
        print("'vogal'")
    else:
        print("'consoante'")


if __name__ == '__main__':
    letra = input('Informe uma letra: ')
    vogal_ou_consoante(letra)
