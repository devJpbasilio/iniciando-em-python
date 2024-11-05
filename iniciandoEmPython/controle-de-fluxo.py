
# Envair um email com os detalhes da compra compra online (maximo 3
# tentativas) para compra confirmadas.

compra_confirmada = False
dados_compras = "Compra no valor de R$12.50 e entraga confirmada"

for enviar in range(3):
    if compra_confirmada:
        print(dados_compras)
        print("Detalhes enviado para seu email")
        break
else:
    print("Falha na compra")

