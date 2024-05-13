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


def somar(*numeros):
    soma=0
    for x in range(len(numeros)):
        soma += numeros[x]
    print(soma)

def texto(argumento):
    cont = len(argumento)
    for x in range(cont):
        if argumento[x] in " .,!?":
            cont = cont - 1
    print(cont)
    print(argumento[::-1])

def lista_unica(l):
    nova_lista=[]
    for x in l:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)

a=[1,2,2,3,4,4,5,3,6,7,6,8]
lista_unica(a)

def duplicados(*lista):
    nova=set(lista)
    print(f"Lista recebida {lista}")
    print(f"A lista sem repetição {nova}")

def dupli2(l):
    listaNova=[]
    for x in lista:
        if x not in listaNova:
            listaNova.append(x)
    print(listaNova)


def primo(n):
    if (n==1):
        return n,"não é primo"
    elif (n==2):
        return n,"È primo";
    else:
        for x in range(2,n):
            if(n % x==0):
                return n,"Não é primo"
            return n,"É primo"
