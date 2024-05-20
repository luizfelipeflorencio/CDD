class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calculoArea(self, base, altura):
        self.area = base * altura
        print(f"A area é {self.area}")
    def calculoPerimetro(self,base, altura):
        self.perimetro = 2*(base+altura)
        print(f"O perimetro é {self.perimetro}")

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculoArea(self,base, altura):
        self.area= (base*altura)/2
        print(f"A area é {self.area}")

    def calculoPerimetro(self,altura,base):
        self.perimetro= altura+(base*2)
        print(f"O perimetro é {self.perimetro}")