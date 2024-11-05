"""
Estrutura Condicionais
As Estrutura condicionais permitem executar diferentes blocos de codigos
com base em condições
"""

"""
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print("você é maior de idade")
else:
    print("Você é menor de idade")
"""
def media_semestral(nota_minima = 6.0):
    # Solicito ao usuário o números de notas
    notas_semestral = int(input("Digite o número de notas: "))

    # Inicializa uma lista para armazenar as notas
    notas = []

    # Loop para inserir as notas
    for i in range(notas_semestral):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    #Calcula a média
    media = sum(notas) / notas_semestral

    print(f"A media escolar é: {media:.2f}")

    if media >= nota_minima:
        print("O aluno foi aprovado!")
    else:
        print("O aluno foi reprovado!")

    return media

# Chamando a função
media_semestral()
