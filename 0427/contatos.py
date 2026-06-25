meu_contatos = [
    {"nome": "laura","celular":"555555", "email": "laura@gmail.com"},
    {"nome": "bruno", "celular": "222222", "email":"bruno@gmail.com"},
    {"nome": "Clara", "celular": "111111" , "email": "Clara@gmail.com"}
]

#print(meu_contatos [2] ["nome"], meu_contatos [2] ["email"])
for contato in meu_contatos:
    print(contato["nome"], contato["celular"], contato["email"] )