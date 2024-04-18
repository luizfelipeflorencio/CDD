v1=int(input("digite o primeiro valor: "))
v2=int(input("digite o segundo valor: "))
x = 0
while x < 100000000000:
    if v2==0:
        v2 = int(input("Digite o segundo valor novamente: "))
        x += 1
    else:break
divisao =  v1/v2
print(divisao)