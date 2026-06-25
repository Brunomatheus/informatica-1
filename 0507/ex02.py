lista =[]

while(True):
    print("\n --- Menu ---")
    print("1 - Adicionar compromisso")
    print("2 - lista comprimisso")
    print("3 - sair")

    opcao = input("escolha uma opção: ")

    if (opcao == "1"):
        data = input("Digite a data (DD/MM/AA): ")
        hora = input("digite a hora (HH:MM): ")
        descrisao = input("Digite uma descrisão: ")
        local = input("digite o local: ")

        compromisso = {
            "data": data,
            "hora": hora,
            "descrisao":descrisao,
            "local": local 
        }
        lista.append(compromisso)
        print("compromisso adicionado com sucesso!")

    elif(opcao == "2"):
        if len(lista) == 0:
            print("não á compromissos!")
        else:
            for item in lista:
                print("\n", item["data"], "\n", item["hora"], "\n", item["descrisao"],"\n", item["local"], "\n" )
    elif(opcao == "3"):
        print("encerrando o programa...")
        break

    else:
        print("opção invalido, tente novamente")
