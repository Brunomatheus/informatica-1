#pergunta numero e converte para int
numero = int(input("Digite um número: "))

#Se .. Senão no Python é if ... else
if (numero%2 == 0):
#string formatado : substitui o {numero} pelo valor da variável numero
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")