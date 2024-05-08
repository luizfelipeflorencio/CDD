def cadastro():
    nomes = ["","","","",""]
    senhas = ["","","","",""]
    for x in range(5):
        nomes[x]= input("Digite o nome do usuario: ")
        senhas[x]= input("Digite a senha: ")

def imprime_nome(nome):
    print(f"Nome: {nome}")

def numeros(numero):
    for x in range(numero+1):
        for y in range(x):
            print(x, end=" ")
        print()
    numero = int(input("Digite o numero: "))
    numeros(numero)

def piramide(j):
    for x in range(1,j+1):
        for y in range(1,x+1):
            print(y, end=" ")
        print()
    numero = int(input("Digite o numero: "))
    piramide(numero)


def vogais(texto):
    cont = 0
    for x in texto:
        if x in "aeiouAEIOU":
            cont = cont + 1
    print(cont)
texto = "O rato roeu a roupa do rei de Roma"
vogais(texto)

def estoque(nome, quantidade, preco):
    total= preco * quantidade
    return total