from array import array

# Array (matriz)
    # similar a listas
    # melhor performace


letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40, 50, 60]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u',['a', 'b', 'c', 'd'])
numeros_i = array('i',[10, 20, 30, 40, 50, 60])
numeros_f = array('f',[1.2, 2.2, 3.2])

print(letras)
print(numeros_i)
print(numeros_f)