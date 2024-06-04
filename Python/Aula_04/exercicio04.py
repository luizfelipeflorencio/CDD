negativo = 0
for x in range(1,11):
    numero = float(input(f"Digite {x}° numero: "))
    if numero < 0:
        negativo += 1
print(f"O usuario digitou {negativo} numeros negativos")