from pessoa import Pessoa

class dono_de_cachorro(Pessoa):
    def __init__(self, nome, idade, cpf, endereco):
        super().__init__(nome, idade)

        self.cpf = cpf  
        self.endereco = endereco