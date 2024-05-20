class Pessoa():
    def __init__(self, nome, peso, idade, comendo = False, falando = False, dormindo = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo

    def comer(self, alimento):

        if self.comendo == False and self.falando == False and self.dormindo == False:
            self.comendo = True
            print(f"{self.nome} começou a comer {alimento}")
        elif self.comendo == True:
            print(f"{self.nome} está comendo, não pode comer {alimento} agora.")
        elif self.falando == True:
            print(f"{self.nome} está falando, não pode comer {alimento} agora.")
        elif self.dormindo == True:
            print(f"{self.nome} está dormindo, não pode comer {alimento} agora.")

    def pararDeComer(self):

        if self.comendo == True and self.falando == False and self.dormindo == False:
            self.comendo = False
            print(f"{self.nome} parou de comer")
        elif self.comendo == False and self.falando == False and self.dormindo == False:
            print(f"{self.nome} está fazendo nada")
        elif self.falando == True:
            print(f"{self.nome} não está comendo, está falando")
        elif self.comendo == False and self.falando == False and self.dormindo == True:
            print(f"{self.nome} não está comendo, está dormindo")

    def falar(self):

        if self.comendo == False and self.falando == False and self.dormindo == False:
            self.falando = True
            print(f"{self.nome} começou a falar")
        elif self.falando == True:
            print(f"{self.nome} está falando")
        elif self.comendo == True:
            print(f"{self.nome} está comendo, não pode falar")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar, está dormindo")

    def pararDeFalar(self):
        if self.comendo == False and self.falando == True and self.dormindo == False:
            self.falando = False
            print(f"{self.nome} parou de falar")
        elif self.comendo == True:
            print(f"{self.nome} está comendo")
        elif self.dormindo == True:
            print(f"{self.nome} está dormindo")
        elif self.comendo == False and self.falando == False and self.dormindo == False:
            print(f"{self.nome} está fazendo nada")

    def dormir(self):
        if self.comendo == False and self.falando == False and self.dormindo == False:
            self.dormindo = True
            print(f"{self.nome} foi dormir")
        elif self.comendo == True:
            print(f"{self.nome} está comendo, não pode ir dormir")
        elif self.falando == True:
            print(f"{self.nome} está falando, não pode ir dormir")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo")

    def acordar(self):
        if self.comendo == False and self.falando == False and self.dormindo == True:
            self.dormindo = False
            print(f"{self.nome} Acordou")
        elif self.comendo == True:
            print(f"{self.nome} está acordado e comendo")
        elif self.falando == True:
            print(f"{self.nome} está acordado e falando")
        elif self.comendo == False and self.falando == False and self.dormindo == False:
            print(f"{self.nome} está fazendo nada")