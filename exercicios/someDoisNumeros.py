
def somar_dois_numeros(a, b):
    return a + b


def subtrair_dois_numeros(a, b):
    print(f'A subtração entre {a} e {b} é {a - b}')


num1 = int(input('Entre com o primeiro número: '))
num2 = int(input('Entre com o segundo número: '))

soma = somar_dois_numeros(num1, num2)

print(f'A soma entre {num1} e {num2} é {soma}')
subtrair_dois_numeros(num1, num2)