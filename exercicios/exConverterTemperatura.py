
def converter_temperatura(celsius):
    tf = celsius * 1.8 + 32
    return f'{tf:.2f}'


temperatura = float(input('Digite a temperatura em Celsius: '))
print(f'A temperatura em Fahrenheit {converter_temperatura(temperatura)}')