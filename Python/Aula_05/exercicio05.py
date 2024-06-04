num = int(input("Digite um número: "))
for x1 in range(1, num + 1):
    for x2 in range(x1):
        print(x1, end=' ')

 #ou

num = int(input("Digite um numero: "))
for x in range(1, num +1):
    for y in range(1, x+1):
        print(x, end=' ')