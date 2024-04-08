hora1 = int(input("Primeira Hora:"))
minuto1 = int(input("Primeiros Minutos:"))
hora2 = int(input("Segundo Hora:"))
minuto2 = int(input("Segundos Minutos:"))

if hora1 >= 12:
    hora1 -= 12

if hora2 >= 12:
    hora2 -=12

horas = hora1 + hora2
minutos = minuto1 + minuto2

if minutos >= 60:
    minutos -= 60
    horas += 1

if minutos < 10:
    print(f"{int(horas)}:0{minutos}")
else:
    print(f"{int(horas)}:{minutos}")
