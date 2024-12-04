from sys import getsizeof

numeros = [x * 10 for x in range(100)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print('=======')

numeros = (x * 10 for x in range(100))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))