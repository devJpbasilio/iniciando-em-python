
''' __init__ é o método especial chamado  quando um objeto é criado.
É onde você inicializa os atributos.
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Metodo
    def apresentar(self):
        print(f'Olá, {self.nome} você tem {self.idade} anos.')


# Criando objetos



print("")
# Herança permite criar novas classes baseadas em outras.
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo


    def apresentar_cargo(self):
        print(f'Olá, {self.nome} você tem {self.idade} anos e trabalha como {self.cargo}')


func1 = Funcionario(input('Nome: '), int(input('Idade: ')), input('Cargo: '))
Funcionario.apresentar_cargo(func1)

