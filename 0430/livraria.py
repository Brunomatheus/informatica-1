livros = []


while(True):
    titulo = input("digite o titulo do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = int(input("Digite o ano de publicação do livro: "))
    disponivel = input("o livro esta disponivel sim/não: ")

    if(disponivel == "sim"):
        disponivel = True
    else:
        disponivel = False
    
    livros.append({'titulo':titulo, 'autor':autor, 'ano de publicação':ano_publicacao, 'disponivel': disponivel})

    continuar = input("deseja continuar s/n: ").upper()
    if(continuar != "S"):
        break
for livro in livros:
    print(f"\ntitulo: {livro['titulo']}, autor: {livro['autor']}, ano de publicação: {livro['ano de publicação']}, {livro['disponivel']} ")

