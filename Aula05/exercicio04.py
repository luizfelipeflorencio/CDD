resposta = 's'
while resposta == 's' or resposta == 'S':
    nota1 = float(input("Digite a 1 nota: "))
    while nota1 <0 or nota1 >10:
        nota1 = float(input("Digite a 1 nota nnovamente: "))
    nota2 = float(input("Digote a 2 nota: "))
    while nota2 <0 or nota2 >10:
        nota2 = float(input("Digite a 2 nota novamente: "))
    media = (nota1+nota2)/2
    print(media)
    resposta = input("Deseja realizar um novo calculo?(S/N): ")