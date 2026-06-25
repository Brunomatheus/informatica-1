#pergunta ao usuário o valor da compra. converte para float (número com decimal)
valor_compra = float(input("Qual o valor da compra? "))

#a variável frete_gratis vai receber um valor bool: ou True ou False
frete_gratis = valor_compra >= 150

print("Frete grátis: ", frete_gratis)