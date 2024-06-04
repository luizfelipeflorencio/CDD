ano = int(input("digite o ano que nasceu: "))
mes = int(input("Digite o mês: "))
dia = int(input("Digite o dia: "))

anoAtual= 2024
mesAtual= 4
diaAtual= 24

if mes < mesAtual:
    idade = anoAtual - ano
elif mes == mesAtual:
    if diaAtual <= diaAtual:
        idade = anoAtual - ano
    else:
        idade = anoAtual - ano - 1
else:
    idade = anoAtual - ano - 1


print("Sua idade é:",idade)
