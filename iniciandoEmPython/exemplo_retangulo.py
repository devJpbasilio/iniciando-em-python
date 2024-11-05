"""
Criar um retângulo de 3x12
@@@@@@@@@@@@
@@@@@@@@@@@@
@@@@@@@@@@@@
"""

linhas = 3
colunas = 12
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()