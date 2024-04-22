vezes = "S"
while vezes == "S" or vezes == "s":
    base = float(input("Digite a base do triangulo: "))
    altura = float(input("Digite a altura do triangulo: "))
    a = (base*altura)/2
    print("A area do triangulo é:",a)
    vezes = input("Gostaria de fazer novamente (S/N): ")