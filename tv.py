class TV:
    def __init__(self,  controle, status=0, canal=0):
        self.controle = controle
        self.status = status
        self.canal = canal

    def ligar(self):
        if self.status == 0:
            self.status += self.controle.ligar() 
            return self.status
        else:
            self.status -= self.controle.desligar()
            return self.status

    def proximo_canal(self):
        if self.status == 1 and self.canal < 100:
            self.canal += self.controle.canal_proximo()
            return self.canal
        elif self.status == 1 and self.canal > 99:
            self.canal = 0
            return self.canal
    