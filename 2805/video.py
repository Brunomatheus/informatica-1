videos = []

def registrar():
    print("Adicionando videos... ")
    titulo = input("Informe o titulo: ")
    tema = input("Digite o tema: ")
    duracao = int(input("Escreva a duração minutos: "))
    status = input("descreva o status (1) - Gravado, (2) - não gravado: ")
    if(status == "1"):
        status = "Gravado"
    elif(status == "2"):
        status = "Não gravado"
    
    listar = {
        "titulo": titulo,
        "tema": tema,
        "duracao": duracao,
        "status": status
             
    }

    videos.append(listar)
def listar_videos():
    for video in videos:
        print("video(s): ")
        print("Titulo: ",video["titulo"] )
        print("Tema: ",video["tema"] )
        print("duração: ",video["duracao"] )
        print("Status: ",video["status"] )

    if(len(videos) == 0):
        print("Não á videos para listar")
def filtrar_videos():
    filtrar = input("digite qual Status deseja filtrar (1) - Gravado, (2) - Não gravado: ")
    if(filtrar == "1"):
        filtrar = "Gravado"
    elif(filtrar == "2"):
        filtrar = "Não gravado"

    for filtro in videos:
        if(filtrar == filtro["status"]):
            print("Status: ", filtro["status"])
            print("Titulo: ",filtro["titulo"] )
            print("Tema: ",filtro["tema"] )
            print("duração: ",filtro["duracao"] )
            print("Status: ",filtro["status"] )
            return
        else:
            print("Videos não encontrados")
            return
    else:
        print("Status de video não encontrado")
def calcular_tempo():
    soma = 0
    calcular = input("digite qual Status deseja Calcular (1) - Gravado, (2) - Não gravado: ")
    if (calcular == "1"):
        calcular = "Gravado"
    elif(calcular == "2"):
        calcular = "Não gravado"
    for filtro in videos:
        if(calcular == filtro["status"]):
            soma += filtro["duracao"]
            print("Calculando soma de video ", filtro["status"])
            print(f"A soma do tempo do video {filtro["status"]} é de {soma} minutos")
            return
    else:
        print("Status de video não encontrado")
def atualizar_status():
    nome_video = input("digite o nome do video que deseja atualizar: ")
    for video in videos:
        if (video["titulo"].lower() == nome_video.lower() ):
            video["status"] = "Gravado"
            print(f"O video {video["titulo"]} teve o status atualizado pra Gravado")
            return
        else:
            print("Nome do video não encontrado!")
while(True):
    print("--- Menu ---")
    print("(1) - Registrar videos")
    print("(2) - listar videos")
    print("(3) - Filtrar videos")
    print("(4) - Calcular tempo de videos")
    print("(5) - Atualizar status")
    
    opcao = input("Digite a opção que deseja: ")

    if(opcao == "1"):
        registrar()
    elif(opcao =="2"):
        listar_videos()
    elif(opcao == "3"):
        filtrar_videos()
    elif(opcao == "4"):
        calcular_tempo()
    elif(opcao == "5"):
        atualizar_status()
    else:
        print("opção incorreta escolha outra!")

