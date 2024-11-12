
valores = [30, 8.50, 9.99, 9.99, 9.99, 10, 8.99]
produtos = ['Arroz', 'Feijão', 'Laranja', 'Banana', 'Maçã', 'Abacate', 'Uva']

'''
ZIP combina as duas listas em pares. O zip cria 
uma sequencia de tuplas, onde o primiro elemento de cada tupla 
é de produto e o segundo é de valores
[('Arroz', 30), ('Feijão', 8.50), ('Laranja', 9.99), ...]
'''
for x, y in zip(produtos, valores):
    print(f'Os valores do {x} é de R$ {y:.2f} ')
