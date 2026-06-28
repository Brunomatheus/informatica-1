aluno = []
def cadastrar_aluno(aluno):
    nome = input("Digite seu nome: ")
    turma = input("Digite a sua turma: ")
    nota1 = int(input("Digite a sua primeira nota: "))
    nota2 = int(input("Digite a sua segunda nota: "))
    media = 0
    media = (nota1 + nota2)/2
    listar = {
        "nome":nome,
        "turma":turma,
        "nota1":nota1,
        "nota2":nota2,
        "media":media
    }
    aluno.append(listar)
def media_aluno(aluno):
    if(len(aluno) == 0):
        print("Nenhum aluno ainda cadastrado.")
        return
    perguntar = input("Digite o nome do aluno que deseja ver a media: ")
    media = 0
    for alunos in aluno:
        if(perguntar.lower() == alunos["nome"].lower()):
            media = (alunos["nota1"] + alunos["nota2"])/2
            alunos["media"] = media
            print(f"A media do aluno é {media}")
            return
    else:
        print("Nome de usuario não encontrado!")    
        
def listar_aluno(aluno):
    if(len(aluno) == 0):
        print("Nenhum aluno ainda cadastrado.")
        return
    print("--- Listando alunos ---")
    for alunos in aluno:
        print(f"Aluno(a): {alunos["nome"]}")
        print(f"Turma: {alunos["turma"]}")
        print(f"Media: {alunos["media"]}")

def aprovados(aluno):
    if(len(aluno) == 0):
        print("Nenhum aluno ainda cadastrado.")
        return
    for alunos in aluno:
        if(alunos["media"] >= 7 ):
             print(f"Aluno(a): {alunos["nome"]} aprovado")
             
        else:
            print("Nenhum aluno foi aprovado!")
while(True):
    print("--- Menu ---")
    print("(1) - Cadastrar aluno")
    print("(2) - Ver media do aluno")
    print("(3) - Listar alunos")
    print("(4) - Alunos aprovados")
    opcao = input("Digite a opção: ")
    if(opcao == "1"):
        cadastrar_aluno(aluno)
    elif(opcao == "2"):
        media_aluno(aluno)
    elif(opcao == "3"):
        listar_aluno(aluno)
    elif(opcao =="4"):
        aprovados(aluno)

        
    