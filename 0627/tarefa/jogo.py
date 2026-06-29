jogo = []

def cadastrar_jogo(jogo):
    nome = input("Digite o nome do jogo: ")
    genero =  input("digite o genero do jogo: ")
    horas = int(input("digite o numero de horas jogadas: "))
    listar = {
        "nome":nome,
        "genero":genero,
        "horas":horas,

    }
    jogo.append(listar)
def listar_jogos(jogo):
    if len(jogo) == 0:
        print("Nenhum jogo cadastrado.")
        return
    for jogos in jogo:
        print("Jogo(s):")
        print(f"Nome: {jogos['nome']}")
        print(f"Genero: {jogos['genero']}")
        print(f"Horas: {jogos['horas']}")
def soma_horas(jogo):
    if len(jogo) == 0:
        print("Nenhum jogo cadastrado.")
        return
    soma = 0
    for jogos in jogo:
        soma += jogos["horas"]
    print(f"A soma de horas jogadas é: {soma}")
    
def jogo_mais_jogado(jogo):
    if len(jogo) == 0:
        print("Nenhum jogo cadastrado.")
        return

    maior = jogo[0]

    for jogos in jogo:
        if jogos["horas"] > maior["horas"]:
            maior = jogos

    print("=== Jogo Mais Jogado ===")
    print(f"Nome: {maior['nome']}")
    print(f"Gênero: {maior['genero']}")
    print(f"Horas jogadas: {maior['horas']}")

while(True):
    print("--- menu ---")
    print("(1) - Adicionar jogo")
    print("(2) - Listar jogo")
    print("(3) - calcular horas jogadas")
    print("(4) - jogo mais jogado")
    perguntar = input("Digite uma opção: ")

    if(perguntar == "1"):
        cadastrar_jogo(jogo)
    elif(perguntar == "2"):
        listar_jogos(jogo)
    elif(perguntar == "3"):
        soma_horas(jogo)
    elif(perguntar == "4"):
        jogo_mais_jogado(jogo)