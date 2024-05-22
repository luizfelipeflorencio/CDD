class PedraPapelTesoura():
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogada1 = ""
        self.jogada2 = ""

    def resultado(self, primeiraJogada, segundaJogada, ponto):
        self.jogada1 = primeiraJogada.lower()
        self.jogada2 = segundaJogada.lower()
        self.ponto = 0
    def contador(self):
        if self.jogador1 == self.ponto == 3:
            print(f"{self.jogador1} marcou 3 ponto primeiro e ganhou")
        elif self.jogador2 == self.ponto == 3:
            print(f"{self.jogador2} marcou 3 ponto primeiro e ganhou")

            if self.jogada1 == "pedra" and self.jogada2 == "pedra":
                print("Empate nenhum marcou ponto")

            elif self.jogada1 == "pedra" and self.jogada2 == "papel":
                print("Papel venceu")

            elif self.jogada1 == "pedra" and self.jogada2 == "tesoura":
                print("Pedra venceu")

            elif self.jogada1 == "papel" and self.jogada2 == "papel":
                print("Empate")

            elif self.jogada1 == "papel" and self.jogada2 == "pedra":
                print("Papel venceu")

            elif self.jogada1 == "papel" and self.jogada2 == "tesoura":
                print("Tesoura venceu")

            elif self.jogada1 == "tesoura" and self.jogada2 == "tesoura":
                print("Empate")

            elif self.jogada1 == "tesoura" and self.jogada2 == "papel":
                print("Tesoura venceu")

            elif self.jogada1 == "tesoura" and self.jogada2 == "pedra":
                print("Pedra venceu")

            else:
                print("Tente Novamente")