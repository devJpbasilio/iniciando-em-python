
# == While Loops ==

# Excelente para loops dependentes de uma condição.

# Criar uma promoção para um produto no valor de R$200.

valor = 200
dia = 0
while valor > 20:
    dia += 1
    print(f'Dia {dia} o produto vai ser vendido por R${valor}')
    valor -= 5