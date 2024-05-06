numeros = [0,0,0,0,0]
for x in range(5):
    numeros[x] = int(input("Digite o numero: "))

for y in range(4,-1,-1):
    print(numeros[y], end=" ")