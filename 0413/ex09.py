saldo = 0
opcao = 1

while (opcao != 3):
    print("\nfinalizando...")
    
    if (opcao == 1):
        print(f"\ seu saldo é: {saldo}")
    elif(opcao == 2 ):
        valor_deposito = float (input("valor deposito: "))
        saldo += valor_deposito
    elif(opcao == 3):
       
    else:
        print("\nopcão invalida")
    opcao = int(input("\n (1) - saldo\t(2) - deposito\t(3) - sair: \n"))