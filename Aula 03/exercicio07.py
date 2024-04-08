soma = 0
for x in range(1,11):
    numero = int(input("Digite um número: "))
    if numero % 2 != 0:
        soma = soma + numero
print(soma)