numero = int(input("digite um numero entre 1 e 10: "))

if (numero < 1 or numero > 10 ):
        print("numero invalido, escreva entre um numero entre 1 e 10")
else:       
     for i in range(1, 11):
         print(f"{numero} x {i} = {numero*i}")
    

        