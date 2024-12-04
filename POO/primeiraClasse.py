from importlib.metadata import pass_none


# Classes
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma class
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar


# criar a classe
class Funcionario:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento


    def apresentar(self):
        print(f'Nome: {self.nome} \nSobrenome: {self.sobrenome} \nData de Nascimento: {self.data_nascimento}')


# criar o objeto
usuario1 = Funcionario('Elena', 'Cabral', '12/01/2009')
usuario1.apresentar()