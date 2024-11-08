
# Lista de uma determinada seção de supermacado

secaoBebidas = ['Refrigerante', 'vinhos', 'Sucos', 'Agua',
                'Cervejas Nacionais', 'Cervejas Importadas',
                'Whisky', 'Vodca', 'Conhaque']


# Funções dentro de listas
secaoBebidas.append('Groselha') # função para add um item ao final da lista
secaoBebidas.remove('Vodca') # função para remover um item da lista
secaoBebidas.insert(7, 'Energéticos') #add um item na lista através do index
secaoBebidas.sort()


for bebidas in secaoBebidas:
    print(bebidas)