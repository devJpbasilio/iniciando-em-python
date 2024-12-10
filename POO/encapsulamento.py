'''

O encapsulamento controla o acesso aos atributos de um objeto:
    * Público: acessível de qualquer lugar(ex:self.nome)
    * Protegido: usa um _ antes do nome(ex:_atributo)
    * Privado: usa __ antes do nome(ex:__atributo)
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo # Atributo privado


    def depositar(self, valor):
        self. __saldo += valor
        print(f'depósito de R$ {valor:.2f} realizado com sucesso')


    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de {valor:.2f} realizado com sucesso')
        else:
            print('Saldo insuficiente.')


    def exibir_saldo(self):
        print(f'Saldo Atual: {self.__saldo:.2f}')


# Testando a classe

conta = ContaBancaria("João", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(250)
conta.exibir_saldo()