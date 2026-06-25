notas = []

while(True):
    nota = float(input("digite as notas: "))
    if (nota < 0):
        break
    elif(nota > 10):
        continue
    else:
        notas.append(nota)

    print(f'a soma das notas é:  {sum(notas)/len(notas)}')
    print(f"a maior nota da turma é {max }")
    print(f"a menor nota da turma é {min}")
