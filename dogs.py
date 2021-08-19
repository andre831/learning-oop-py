from time import sleep
from animal import Animal

class chiuaua(Animal):
    def __init__( self,nome, raca, sex, cor):
        super().__init__(nome, raca, sex, cor)

    def latir(self, som = 'AUAU'):
        print(som)


class pit_bull(Animal):
    def __init__( self, nome, raca, sex, cor):  
        super().__init__( nome, raca, sex, cor)

    def latir(self, som = 'AUAU'):
        print(som)


class pastor_alemao(Animal):
    def __init__( self, nome, raca, sex, cor):
        super().__init__( nome, raca, sex, cor)

    def latir(self, som = 'AUAU'):
        print(som)