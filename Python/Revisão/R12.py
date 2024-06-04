eleitores=int(input("Quantos eleitores: "))
votosBrancos=int(input("Quantos votos brancos: "))
votosValidos=int(input("Quantos votos validos: "))
votosNulos=int(input("Quantos votos nulos: "))

totalEleitores= votosBrancos + votosValidos + votosNulos

while totalEleitores < eleitores:
    votosValidos=int(input("Quantos votos validos: "))
    totalEleitores = votosBrancos + votosValidos + votosNulos

porcBrancos= 100 * (votosBrancos/eleitores)
porcValidos= 100 * (votosValidos/eleitores)
porcNulos= 100 * (votosNulos/eleitores)

print(f"A porcentagem de votos brancos foram:{porcBrancos}")
print(f"A porcentagem de votos validos foram:{porcValidos}")
print(f"A porcentagem de votos nulos foram:{porcNulos}")