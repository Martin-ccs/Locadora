from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, numero_portas: int, ar_condicionado: bool):
        super().__init(placa, modelo, ano, diaria_base, status, categoria_cnh_exigida)

        self.__numero_portas = numero_portas
        self.__ar_condicionado = ar_condicionado

    @property
    def numero_portas(self):
        return self.__numero_portas

    @property
    def ar_condicionado(self):
        return self.__ar_condicionado
