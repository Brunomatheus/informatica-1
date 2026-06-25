#pergunta o ano de nascimento do jogador. converte para int.
ano_nascimento = int(input("Seu ano de nascimento: "))

#calculamos a idade subtraindo de 2026(ano atual) a data de nascimento
idade = 2026 - ano_nascimento

#variável assume um valor bool (True ou False)
pode_jogar = idade >= 16

print("Pode jogar:", pode_jogar)