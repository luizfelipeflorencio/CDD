x = 0
soma = 0
while x < 10:
    x += 1
    num = int(input(f"Digite {x}° numero: "))
    soma = soma + num
media = soma / x
print(media)