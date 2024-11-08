
def palindromo(palavra):
    fraseInvertida = palavra[::-1]
    return fraseInvertida


frase = str(input('Digite uma frase ou digite uma palavra: ')).strip().upper()

caracteres = ''.join(frase.split())

resultado = palindromo(caracteres)

print(f'{caracteres}, {resultado}')

if caracteres == resultado:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')