from exercicio01 import vogais
h = "eu to doido"
print(h)

from exercicio01 import estoque
produto = input("Digite o produto: ")
quant = int(input("Digite a quantidade: "))
valor = float(input("Digite o preço: "))
retorno = estoque (produto,quant,valor)
soma = 0
soma = soma + retorno