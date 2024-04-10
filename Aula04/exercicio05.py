dentroIntervalo = 0
foraIntervalo = 0
for x in range(1, 11):
    numero = int(input(f"Digite {x}° numero: "))
    if numero >= 10 and numero <= 20:
        dentroIntervalo += 1
    else:
        foraIntervalo += 1

print(f"Estão dentro do intervalo: {dentroIntervalo} numeros")
print(f"Estão fora do intervalo: {foraIntervalo} numeros")

#melhor forma para quem esta aprendendo

dentroIntervalo = 0
foraIntervalo = 0
for x in range(1, 11):
    numero = int(input(f"Digite {x}° numero: "))
    if numero >= 10 and numero <= 20:
        dentroIntervalo += 1
    foraIntervalo += 1

print(f"Estão dentro do intervalo: {dentroIntervalo} numeros")
print(f"Estão fora do intervalo: {foraIntervalo} numeros")
