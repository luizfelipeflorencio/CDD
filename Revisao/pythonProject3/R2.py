soma = 0
for x in range(2):
    notas = float(input("Digite a nota: "))
    soma = soma + notas
    media = soma /2
if media >= 7:
    print("Aluno aprovado")
elif media >= 4:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")