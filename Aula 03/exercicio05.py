numero = int(input("Digite um número: "))
print(f"A tabuada de {numero} é: ")
for x in range(1,11):
    multi = numero * x
    print(f"{numero}x{x}={multi}")