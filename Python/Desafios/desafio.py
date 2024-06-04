opcao = -5
nomes = ["","","","",""]
senhas = ["","","","",""]
cont = 0

while opcao != 3:
    opcao =int(input("1 para cadastrar\n"
                     "2 para login\n"
                     "3 para sair\n"
                     "Escolha sua opção: "))

    if opcao == 1:
        for x in range(5):
            nomes[x]= input("Digite o nome do usuario: ")
            senhas[x]= input(f"Digite a senha de {nomes[x]}: ")


    elif opcao == 2:
        login = input("Digite o usuario: ")
        senha = input("Digite a senha: ")
        for y in range(5):
            if login == nomes[y]:
                if senha == senhas[y]:
                    print("Login realizado com sucesso!")
                else:
                    print("senha incorreta!")
            else:
                cont = cont + 1
        if cont == 5:
            print("Usuario não existe!")