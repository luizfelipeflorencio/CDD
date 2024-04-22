vezes = "S"
while vezes == "S" or vezes == "s":
    num=int(input("Digite um numero: "))
    while num == 0:
        num = int(input("Digite um numero que não seja 0: "))
    if num > 0:
        print("Numero positivo")
    else:
        print("Numero negativo")
    vezes=input("Gostaria de fazer novamente (S/N): ")