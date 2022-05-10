"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Square():
    def __init__(self, side):
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_side):
        self.__side = new_side

    def area(self):
        return self.__side ** 2
