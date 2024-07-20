"""
Exercício 07 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
Mostrar a área com 2 casas decimais.

    >>> from secao_01_estrutura_sequencial import ex_07_area_quadrado
    >>> ex_07_area_quadrado.input = lambda k: '2'
    >>> ex_07_area_quadrado.calcular_area_de_quadrado()
    A área do quadrado com esse lado é: 4.00
    O dobro da área do quadrado é: 8.00
    >>> ex_07_area_quadrado.input = lambda k: '2.5'
    >>> ex_07_area_quadrado.calcular_area_de_quadrado()
    A área do quadrado com esse lado é: 6.25
    O dobro da área do quadrado é: 12.50

"""


def calcular_area_de_quadrado():
    """Escreva aqui em baixo a sua solução"""
    lado = float(input('Informe o lado do quadrado: '))
    area_quadrado = lado * lado
    dobro_da_area = area_quadrado * 2

    print(f'A área do quadrado com esse lado é: {area_quadrado:2.2f}')
    print(f'O dobro da área do quadrado é: {dobro_da_area:2.2f}')
