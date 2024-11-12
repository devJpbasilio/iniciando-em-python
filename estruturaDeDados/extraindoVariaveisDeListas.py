
# Unpacking Lists
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

produtos = ['Arroz', 'Feijão', 'Laranja', 'Banana']

'''item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]
'''

item1, item2, item3, *outros = produtos
#item1, item2, item3, item4 = produtos

print(item1)
print(item2)
print(item3)
#print(item4)
print(outros)