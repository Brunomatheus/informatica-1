itens = int(input("digite a quantidade de itens que voce quer adicionar:  "))
lista = ""
for i in range(itens):
    
    nome = input("digite o nome dos itens: ")
    lista = lista + ' ' + nome
    
print(f"o lista ficou assim: {lista}")