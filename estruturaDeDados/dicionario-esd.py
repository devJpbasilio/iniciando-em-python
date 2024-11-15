
# Dicionários
    # Utiliza index no formato de Keys e values
    # Aceita string, integer, float, boolean...

aluno = {'nome': 'Joao',
         'Idade': '16',
         'nota_final': 'A',
         'situacao': 'Aprovado'}
'''
Troncando valor:
aluno['nome'] = 'Ana'

Outra forma:
aluno.update({'nome': 'Carlos', 'nota_final': 'B'})
'''
aluno['nome'] = 'Ana'
aluno.update({'nome': 'Carlos', 'nota_final': 'B'})

print(aluno)