#pergunta a temperatura do paciente
temperatura = float(input("Qual a temperatura do paciente: "))

if (temperatura > 37.5):
    print(f"Temperatura: {temperatura} - Febre. Encaminhar para o médico.")
else:
    print(f"Temperatura: {temperatura} - Normal. Liberado.")