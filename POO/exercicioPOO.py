# Vamos Criar uma classe para Clientes da Netflix

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        lista_planos = ["basic", "premium"]
        if plano in lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano Inválido")


cliente = Cliente("João", "<joao@gmail.com", "premium")
print(cliente.nome)