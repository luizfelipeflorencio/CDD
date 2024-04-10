alunos = int(input(f"Quantos alunos tem na sala: "))
x = 0
soma = 0
while x < alunos:
    x += 1
    notas = float(input(f"Digite a nota do aluno {x}: "))
    soma = soma + notas
media = soma / alunos
print(media)