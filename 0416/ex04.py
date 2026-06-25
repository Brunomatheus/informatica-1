
palavra = input("Digite uma palavra: ")
vogal = 0 

for i in palavra:
    if i.lower() in "aÁáÂâÀàÃãeÉéÊêiÍíoÓóÔôÕõuÚú":
        vogal+=1


print(f"a palavra tem {vogal} vogais.")
