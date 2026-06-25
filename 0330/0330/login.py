#pergunta para usuário o seu nome e a sua senha
usuario = input("Usuário: ")
senha = input("Senha:")

#o operador lógico and equivale ao e do portugol
#caso o nome do usuário seja "aluno" e a senha "123" entra no if
if (usuario == "aluno" and senha == "123"):
    print("Acesso liberado.")
else:
    print("Acesso negado.")