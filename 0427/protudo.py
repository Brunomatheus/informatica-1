lista = [
    {"nome": "arroz", "preço": 10  , "quantidade": 2},
    {"nome": "feijão", "preço": 20 , "quantidade": 3}

]
total = 0 
for produtos in lista:
    print(f"nome: {produtos["nome"]}, preço: { produtos["preço"]}, quantidade: { produtos["quantidade"]} ")
    total += (produtos["preço"]* produtos["quantidade"])


print("o valor total da compra foi: ", total)