class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno, comendo = False, falando=False, dormindo=False):
        self.nome=nomeAluno
        self.peso=pesoAluno
        self.idade=idadeAluno
        self.comendo=comendo
        self.falando=falando
        self.dormindo=dormindo
    def comer(self, alimento):
        print(f"{self.nome} comeu {alimento}")
        self.comendo=True

    def parardecomer(self):
        print(f"{self.nome} parou de comer")
        self.comendo=False

    def falar(self):
        print(f"{self.nome} está falando")
        self.falando=True

    def paroudefalar(self):
        print(f"{self.nome} parou de falar")
        self.falando=False

    def dormir(self):
        print(f"{self.nome} foi dormir")
        self.dormindo=True

    def paroudedormir(self):
        print(f"{self.nome} parou de dormir")
        self.dormindo=False