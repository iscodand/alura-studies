"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class Ball():
    def __init__(self, color, circunference, material):
        self.__color = color
        self.__circunference = circunference
        self.__material = material
        print(
            f'A bola é {self.__color}, tem {self.__circunference} cm e é feita de {self.__material}.')

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color
        return f'\nA bola agora é {new_color}'
