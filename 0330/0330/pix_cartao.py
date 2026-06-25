forma_pagto = input("Forma pago (P-Pix CC-Cartão de crédito): ")

if (forma_pagto.upper() == 'P'):
    print(f"Pix. Desconto de 15%: {(200* 0.85)}")
elif (forma_pagto.upper() == 'CC'):
    print("Cartão. Valor normal: 200.")
else:
    print("Forma de pagamento inválida.")