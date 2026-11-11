from Pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self, nome: str, cpf: str, matricula: str):
        super().__init__(nome, cpf)
        
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula