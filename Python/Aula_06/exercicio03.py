nota= ['','','','','']
soma=0
cont=0
for x in range(5):
    nota[x]= float(input("Digite a nota: "))

for y in range(5):
    soma = soma + nota[y]
media = soma /5

for z in range(5):
    if nota[z] >= media:
        cont = cont + 1
print(f"A media da sala foi {media} e {cont} alunos foram aprovados")