time1 = input("Nome do time: ")
GolsDoTimeDaCasa = int(input("Números de gols: "))
time2 = input("Nome do time: ")
GolsDoTimeDeFora = int(input("Números de gols: "))

if GolsDoTimeDaCasa == GolsDoTimeDeFora:
    print(f"Empate {time1} {GolsDoTimeDaCasa} X {time2} {GolsDoTimeDeFora}")
elif GolsDoTimeDaCasa > GolsDoTimeDeFora:
    print(f"Vitoria do {time1} por {GolsDoTimeDaCasa} X {GolsDoTimeDeFora}")
else:
    print(f"Vitoria do {time2} por {GolsDoTimeDeFora} X {GolsDoTimeDaCasa}")