litros = float(input("Quantos litros: "))
tipoDeCombustivel = input("E (etanol) ou G (gasolina):")
etanol = litros * 4.9
gasolina = litros * 5.8
if tipoDeCombustivel == "E" or tipoDeCombustivel == "e":
    print(f"Valor total: {etanol}")
elif tipoDeCombustivel == "G" or tipoDeCombustivel == "g":
    print(f"Valor total: {gasolina}")
else:
    print(f"Defina o tipo de combustivel correto: E ou G")