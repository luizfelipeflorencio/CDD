soma = 0
for x in range(1,11):
    numero = int(input(f"Digite {x} numero: "))
    soma = soma + numero
media = soma / x
print(media)