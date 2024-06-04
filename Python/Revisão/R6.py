vezes = "S"
while vezes == "S" or vezes == "s":
    num=int(input("Digite um numero: "))
    calc= num %2
    if calc == 0:
        print("Par")
    else:
        print("Impar")
    vezes=input("Gostaria de fazer novamente (S/N): ")