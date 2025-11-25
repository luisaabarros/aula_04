# ATIVIDADE 1

valor = float(input('Qual o valor da compra? '))

desconto = float(valor * 0.16)

valor_final = float(valor - desconto)

if valor > 250:
    print(f'Houve um desconto de {desconto} e o valor final da compra é de {valor_final}.')
else:
    print(f'Não houve desconto, valor final da sua compra é de {valor}.')