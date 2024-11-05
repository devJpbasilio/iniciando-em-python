# Criar uma funcão que soma vários números.

def soma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


numeros = list(map(int, input('Digite os números separados por espaço que deseja somar: ').split()))

resultado = soma(*numeros)
print(f'A soma dos números digitados é {resultado}')