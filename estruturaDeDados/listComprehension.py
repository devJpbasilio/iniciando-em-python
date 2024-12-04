try:
    x = int(input('Digite um valor que deseja ver a tabuada: '))
except ValueError:
    print('ERROR! Entrada incorreta!')
finally:
    print('Programa finalizado')

valores = [x * i for i in range(1, 11)]
#print(valores)

for i, valor in enumerate(valores, start=1):
    print(f'{x} x {i} = {valor}')