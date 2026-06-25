tarefa = []


while(True):
    print("---Menu---")
    print("(1) - Adicionar tarefa")
    print("(2) - Listar tarefas")
    print("(3) - Mostrar tarefa pendente")

    perguntar = input("Qual opção deseja acionar: ")

    if (perguntar == "1"):
        print("adicionando tarefa...")

        descrisao = input("digite uma decrição para a tarefa: ")
        status = input("Digite P(pendende) ou C(concluida)").upper()

        if(status == "C"):
            
            status = "concluida"
        elif(status == "P"):
            
            status = "pendente"

        listar = {
            "descrisao": descrisao,
            "status": status
        }
        tarefa.append(listar)
        print("Tarefa adicionada")

    elif(perguntar == "2" ):
        if len(tarefa) == 0:
            print("\n não á tarefas adicionadas \n")
        else:
            for tarefas in tarefa:
                print("tarefa:\n" ,tarefas["descrisao"], "\n",tarefas["status"])

    elif(perguntar == "3"):
       for tarefas in tarefa:
           if(tarefas["status"].strip() == "P"):
               print(tarefas["status"]) 
       
  
