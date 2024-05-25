class JogoDaVelha():
    def __init__(self,jogador1,jogador2):
        self.jogador1=jogador1
        self.jogador2=jogador2
        self.escolhaDojogador1= "X"
        self.escolhaDojogador2= "O"

    def resultado(self):
        matriz = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        listaDeJogada = []
        rodadas = 1
        vitoriaDoJogador1 = 0
        vitoriaDoJogador2 = 0

        print(f"{self.jogador1} = X \n{self.jogador2} = O")
        for x in range(0,3):
            for y in range(0,3):
                print(matriz[x][y], end="")
            print()

        while rodadas <=3:

            if vitoriaDoJogador1 == 2:
                print(f"Vitoria do {self.jogador1}!")
                break
            elif vitoriaDoJogador2 == 2:
                print(f"Vitoria do {self.jogador2}!")
                break

            print(f"Inicio da {rodadas} Rodada:")
            rodadas += 1

            for rodada in range(9):

                jogadaDojogador1 = input(f"{self.jogador1} Escolha de 1 a 9: ")

                while jogadaDojogador1 in listaDeJogada:
                    jogadaDojogador1 = input(f"{self.jogador1} Essa jogada ja foi escolhida, escolha outro numero: ")

                while jogadaDojogador1 not in ["1","2","3","4","5","6","7","8","9"]:
                    jogadaDojogador1 = input("Jogada invalida, escolha de 1 a 9: ")

                listaDeJogada.append(jogadaDojogador1)
                print(listaDeJogada)

                if jogadaDojogador1 == "1":
                    matriz[0][0] = self.escolhaDojogador1
                elif jogadaDojogador1 == "2":
                    matriz[0][1] = self.escolhaDojogador1
                elif jogadaDojogador1 == "3":
                    matriz[0][2] = self.escolhaDojogador1
                elif jogadaDojogador1 == "4":
                    matriz[1][0] = self.escolhaDojogador1
                elif jogadaDojogador1 == "5":
                    matriz[1][1] = self.escolhaDojogador1
                elif jogadaDojogador1 == "6":
                    matriz[1][2] = self.escolhaDojogador1
                elif jogadaDojogador1 == "7":
                    matriz[2][0] = self.escolhaDojogador1
                elif jogadaDojogador1 == "8":
                    matriz[2][1] = self.escolhaDojogador1
                elif jogadaDojogador1 == "9":
                    matriz[2][2] = self.escolhaDojogador1

                if rodada >=2:
                    if (matriz[0][0]=="X" and matriz[0][1]=="X" and matriz[0][2]=="X") \
                        or (matriz[1][0]=="X" and matriz[1][1]=="X" and matriz[1][2]=="X") \
                        or (matriz[2][0]=="X" and matriz[2][1]=="X" and matriz[2][2]=="X") \
                        or (matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X") \
                        or (matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X") \
                        or (matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X") \
                        or (matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X") \
                        or (matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X"):

                            print(f"{self.jogador1} Venceu!")
                            vitoriaDoJogador1 +=1
                            print(f"{self.jogador1} - {vitoriaDoJogador1} X {vitoriaDoJogador2} - {self.jogador2}")
                            matriz = [
                                ["1","2","3"],
                                ["4", "5", "6"],
                                ["7", "8", "9"]
                            ]

                            listaDeJogada=[]
                            for x in range(0,3):
                                for y in range(0,3):
                                    print(matriz[x][y], end="")
                                print()
                            print()
                            break
                elif rodada == 9:
                    print("Empate")

                for x in range(0,3):
                    for y in range(0,3):
                        print(matriz[x][y], end="")
                    print()

                jogadaDojogador2 = input(f"{self.jogador2} Escolha de 1 a 9: ")

                while jogadaDojogador2 in listaDeJogada:
                    jogadaDojogador2 = input(f"{self.jogador2} Essa jogada ja foi escolhida, escolha outro numero: ")

                while jogadaDojogador2 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    jogadaDojogador2 = input("Jogada invalida, escolha de 1 a 9: ")

                listaDeJogada.append(jogadaDojogador2)
                print(listaDeJogada)

                if jogadaDojogador2 == "1":
                    matriz[0][0] = self.escolhaDojogador2
                elif jogadaDojogador2 == "2":
                    matriz[0][1] = self.escolhaDojogador2
                elif jogadaDojogador2 == "3":
                    matriz[0][2] = self.escolhaDojogador2
                elif jogadaDojogador2 == "4":
                    matriz[1][0] = self.escolhaDojogador2
                elif jogadaDojogador2 == "5":
                    matriz[1][1] = self.escolhaDojogador2
                elif jogadaDojogador2 == "6":
                    matriz[1][2] = self.escolhaDojogador2
                elif jogadaDojogador2 == "7":
                    matriz[2][0] = self.escolhaDojogador2
                elif jogadaDojogador2 == "8":
                    matriz[2][1] = self.escolhaDojogador2
                elif jogadaDojogador2 == "9":
                    matriz[2][2] = self.escolhaDojogador2

                if rodada >= 2:
                    if (matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O") \
                        or (matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O") \
                        or (matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O") \
                        or (matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O") \
                        or (matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O") \
                        or (matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O") \
                        or (matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O") \
                        or (matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O"):
                        print(f"{self.jogador2} Venceu")
                        vitoriaDoJogador2 +=1
                        print(f"{self.jogador1} - {vitoriaDoJogador1} X {vitoriaDoJogador2} - {self.jogador2}")

                        matriz = [
                            ["1", "2", "3"],
                            ["4", "5", "6"],
                            ["7", "8", "9"]
                        ]

                        listaDeJogada =[]

                        for x in range(0,3):
                            for y in range(0,3):
                                print(matriz[x][y], end="")
                            print()
                        print()
                        break

                elif rodada == 9:
                    print("Empate")

                for x in range(0,3):
                    for y in range(0,3):
                        print(matriz[x][y], end="")
                    print()

        else:
            if vitoriaDoJogador1 < vitoriaDoJogador2:
                print(f"Vitoria do {jogadaDojogador2}")
            elif vitoriaDoJogador1 > vitoriaDoJogador2:
                print(f"Vitoria do {jogadaDojogador1}")
            elif vitoriaDoJogador1 == vitoriaDoJogador2:
                print("Jogo acabou em empate")


p1 = JogoDaVelha("Jogador1", "Jogador2")
p1.resultado()