n1=int(input("Digite o primeiro numero: "))
n2=int(input("Digite o segundo numero: "))
n3=int(input("Digite o terceiro numero: "))
if n1 > n2:
    if n1>n3:
        print(n1)
    else:
        print(n3)
elif n2 > n3:
    print(n2)
else:
    print(n3)