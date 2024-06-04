class Conta():
    def __init__(self,numConta,nomeCliente,tipoConta):
        self.numConta=numConta
        self.nomeCliente=nomeCliente
        self.tipoConta=tipoConta
        self.saldo=0
        self.status=True
    def ativar(self, status=False):
        if status == "ativar":
            self.status == True
            print("A conta foi ativada!")

    def desativar(self, status=False):
        if status == "desativar":
            self.status == True
            print("A conta foi desativada!")

    def depositar(self,valor):
        if valor <0:
            print("Erro, você não pode depositar numero negativo!")
        elif self.status==True:
            self.saldo += valor
            print(f"Você Depositou {valor}!")
        else:
            print("A conta não está ativa ainda!")

    def sacar(self,valor):
        if valor <0:
            print("Erro, você não pode sacar numero negativo!")
        elif self.status ==True:
            if self.saldo >=valor:
                self.saldo -=valor
                print(f"Você sacou {valor}!")
            elif self.saldo < valor:
                print("Voce não tem saldo suficiente!")

    def verificar(self):
        if self.status == True:
            print(self.saldo)
        else:
            print("A conta não está ativa")