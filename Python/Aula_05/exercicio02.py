senha = 1234
x = 0
Dsenha = int(input("Digite uma senha de 4 digitos: "))
while Dsenha != senha:
    Dsenha = int(input("Senha errada, digite novamente: "))
    x += 1
    if x == 2 and senha != Dsenha:
        print("Acesso bloqueado, muitas tentativas erradas")
        break
else:
    print("Login realizado com sucesso!")
    