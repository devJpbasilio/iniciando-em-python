'''

O encapsulamento controla o acesso aos atributos de um objeto:
    * Público: acessível de qualquer lugar(ex:self.nome)
    * Protegido: usa um _ antes do nome(ex:_atributo)
    * Privado: usa __ antes do nome(ex:__atributo)
'''

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # Atributo privado


    def depositar(self, valor):