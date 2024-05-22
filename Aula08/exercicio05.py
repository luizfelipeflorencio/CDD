class Ingresso():
    def __init__(self, valor):
        self.valor=valor
    def imprimeValor(self):
        print(f"O valor do ingresso é: {self.valor} reais")
class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    def valorIngressoVip(self):
        self.valor= self.valor + (self.valor /2)
        print(f"O valor do ingresso Vip é: {self.valor} reais")