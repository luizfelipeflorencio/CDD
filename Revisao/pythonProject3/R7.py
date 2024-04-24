#triangulo
sel = 0
while sel != 3:
    sel = int(input("Qual vc quer calcular? triangulo(1), quadrado(2) ou sair do sistema(3): "))
    if sel == 1:
            base = float(input("Digite a base do triangulo: "))
            altura = float(input("Digite a altura do triangulo: "))
            a = (base * altura)/2
            print("A area do triangulo é:",a)
    #quadrado
    if sel == 2:
            altura = float(input("Digite a altura do quadrado: "))
            a = altura * 4
            print("A area do quadrado é:",a)
