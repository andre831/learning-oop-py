from time import sleep
from animal import Dog

class chiuaua(Dog):
    def __init__( self,nome, raca, sex, cor):
        super().__init__(nome, raca, sex, cor)

    def latir(self, som = 'auau'):
        print(som)


class pit_bull(Dog):
    def __init__( self, nome, raca, sex, cor):  
        super().__init__( nome, raca, sex, cor)

    def latir(self, som = 'auau'):
        print(som)  
    

class pastor_alemao(Dog):
    def __init__( self, nome, raca, sex, cor):
        super().__init__( nome, raca, sex, cor)

    def latir(self, som = 'auau'):
        print(som)





