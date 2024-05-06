nomes= ["","","","",""]
senhas= [0,0,0,0,0]
for x in range(5):
    nomes[x]= input("Digite o nome: ")
    senhas[x] = int(input("Digite a senha: "))
for y in range(5):
    print(nomes[y],senhas[y],y)