horaInicio=int(input("Digite a hora inicial: "))
horaFinal=int(input("Digite a hora final: "))

hora1 = 24 - horaInicio
hora2 = 24 - horaFinal

if horaInicio > horaFinal:
    total=hora1 + horaFinal

elif horaInicio < horaFinal:
    total=horaFinal-horaInicio

print(total,"horas jogadas")