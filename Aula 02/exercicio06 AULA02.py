"""entrada01 = 3:45
entrada02 = 14:20
saida = 6:05"""

hora1 = int(input("Primeira Hora:"))
minuto1 = int(input("Primeiros Minutos:"))
hora2 = int(input("Segundo Hora:"))
minuto2 = int(input("Segundos Minutos:"))

horas = hora1 + hora2
minutos = minuto1 + minuto2

if minutos >= 60:
    minutos -= 60
    horas += 1

if horas > 12:
    horas -= 12
elif horas < 12:
    horas +=12

if minutos < 10:
    print(f"{int(horas)}:0{minutos}")
else:
    print(f"{int(horas)}:{minutos}")
