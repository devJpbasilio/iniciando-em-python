
def idade_eleicoes(idade):
    if idade >= 16:
        return f'Voto permitido!'
    else:
        return f'Voto não permitido!'

idade = int(input('Digite sua idade: '))
print(f'Sua idade é {idade}. {idade_eleicoes(idade)}')