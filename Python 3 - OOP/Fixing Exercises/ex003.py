"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""


class Rect():
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, new_base):
        self.__base = new_base

    @property
    def height(self):
        return self.__base

    @base.setter
    def height(self, new_height):
        self.__height = new_height

    def area(self):
        return self.__base * self.__height

    def perimeter(self):
        return self.__base + self.__height


# Principal

base = float(input('\nValor da Base (m): '))
height = float(input('Valor da Altura (m): '))

rect = Rect(base, height)

print(f'\nÁrea = {rect.area()} m².')
print(f'Perímetro = {rect.perimeter()} m.\n')
