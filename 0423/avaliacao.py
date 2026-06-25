notas = []
soma = 0
while(True):
    nota = float(input("digite as notas: "))
    if (nota < 0):
        break
    elif(nota > 10):
        continue
    else:
        notas.append(nota)



if(len(notas) == 0):
    print("não a notas na avaliação")
else:
    menor = notas[0]
    maior = notas[0]
    #print("a maior nota é ", max(notas))
    #print("a menor nota é", min(notas))

for nota in notas:
    if nota < menor:
        mneor = nota
    if nota > maior:
        maior = nota
    soma+= nota
print("a soma das notas é: ", (soma/len(notas)))
print("a maior nota é", maior)
print("a menor nota é ", menor)
