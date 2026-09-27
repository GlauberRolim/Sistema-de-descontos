# Sistema de descontos

#entrada de dados

# Aqui o cliente digita o valor da sua compra
valor_compra = float(input("Digite o valor total da sua compra: "))


#processamento dos dados e saída

# Se o valor da compra for menor que R$200,00 o sistema calculará 5% de desconto
# Ele exibirá na tela o valor do desconto e o valor a pagar já descontado
if valor_compra < 200:
    desconto = valor_compra * 0.05
    valor_total = valor_compra - desconto
    print("O valor do seu desconto é de R$",desconto)
    print("O valor total a pagar é de R$",valor_total)

# Se o valor da compra for menor ou igual R$200,00 ou menor que R$300,00 o sistema calculará 10% de desconto
# Ele exibirá na tela o valor do desconto e o valor a pagar já descontado
elif 200 <= valor_compra < 300:
    desconto = valor_compra * 0.1
    valor_total = valor_compra - desconto
    print("O valor do seu desconto é de R$",desconto)
    print("O valor total a pagar é de R$",valor_total)

# Se o valor da compra for maior ou igual a R$300,00 o sitema calculará 15% de desconto
# Ele exibirá na tela o valor do desconto e o valor a pagar já descontado
else:
    desconto = valor_compra * 0.15
    valor_total = valor_compra - desconto
    print("O valor do seu desconto é de R$",desconto)
    print("O valor total a pagar é de R$",valor_total)