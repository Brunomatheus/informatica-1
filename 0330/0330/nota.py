#pergunta duas notas e converte
nota1 = float(input("Digite a 1a. nota: "))
nota2 = float(input("Digite a 2a. nota: "))

#calcula a média
media = (nota1+nota2)/2

#recebe valor da comparação(bool): True ou False
aprovado = media >= 7.0

print("Aprovado:", aprovado)