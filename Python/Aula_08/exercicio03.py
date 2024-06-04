class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
    def comer(self):
        print(f"O {self.nome} foi comer...")
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f"O {self.nome} foi miar...")
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latiu(self):
        print(f"O {self.nome} fez o Pythoron...")
class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def pular(self):
        print(f"A {self.nome} pulou...")
class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def mugir(self):
        print(f"A {self.nome} fez muuuuuuuuu...")


