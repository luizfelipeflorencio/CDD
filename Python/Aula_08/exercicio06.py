class Atleta():
    def __init__(self,peso):
        self.aposentado=False
        self.peso=peso
        self.aquecendo=False

    def Aposentar(self):
        if self.aposentado == False:
            print("Atleta pode se aposentar!")
        elif self.aposentado == True:
            print("Atleta aposentado!")

    def Aquecer(self):
        if self.aposentado == True:
            print("Atleta aposentado")
        elif self.aposentado == False:
            print("O Atleta vai se aquecer!")

class Corredor(Atleta):
    def Correr(self):
        if self.aposentado == False and self.aquecendo == True:
            print("Atleta pode correr!")
        elif self.aposentado == True and self.aquecendo == False:
            print("Atleta aposentado, não pode correr!")
        elif self.aposentado == False and self.aquecendo == False:
            print("Atleta não está aquecido, não pode correr!")
class Nadador(Atleta):
    def Nadar(self):
        if self.aposentado == False and self.aquecendo == True:
            print("Atleta pode nadar!")
        elif self.aposentado == True and self.aquecendo == False:
            print("Atleta aposentado, não pode nadar!")
        elif self.aposentado == False and self.aquecendo == False:
            print("Atleta não está aquecido, não pode nadar!")

class Ciclista(Atleta):
    def Pedalar(self):
        if self.aposentado == False and self.aquecendo == True:
            print("Atleta pode pedalar!")
        elif self.aposentado == True and self.aquecendo == False:
            print("Atleta aposentado, não pode pedalar!")
        elif self.aposentado == False and self.aquecendo == False:
            print("Atleta não está aquecido, não pode pedalar!")