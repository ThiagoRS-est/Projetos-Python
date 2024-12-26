#class Cachorro():
#    """Classe para simular um cachorro"""
#    def __init__(self,nome,idade):
#        """Método de inicialização"""
#        self.nome = nome
#        self.idade = idade
#    def sente(self):
#        """Ordena que o cachorro sente"""
#        print(self.nome.title() + " está sentado.")
#    def role(self):
#       """Ordena que o cahorro role"""
#       print(self.nome.title() + " acabou de rolar.")

#meu_cachorro = Cachorro("Sucre",9)
#print("Meu cachorro chama-se " + meu_cachorro.nome.title() + ".")
#print(meu_cachorro.nome.title() + " tem " + str(meu_cachorro.idade) +
#      " anos de idade.")
#meu_cachorro.sente()
#meu_cachorro.role()

#class Carro():
#    """Classe para simular um carro"""
#    def __init__(self,ano,fabricante,modelo):
#        """Método de definição de atributos"""
#        self.ano = ano
#        self.fabricante = fabricante
#    self.modelo = modelo
#        self.odometro = 0
#    def apresentacao(self):
#        """Método para descrição elegante do carro"""
#        descricao = str(self.ano) + " " + self.fabricante.title() + " " + self.modelo.title()
#        return descricao
#    def leitura_odometro(self):
#        """Método para apresentação do odômetro"""
#        print("O odômetro do carro está marcando " + str(self.odometro) + 
#              " Kilômetros rodados.")
#meu_carro = Carro(2016,"audi","a4")
#print(meu_carro.apresentacao()) 
#meu_carro.leitura_odometro()
#meu_carro.odometro = 609
#meu_carro.leitura_odometro()

class Carro():
    """Classe para simular um carro"""
    def __init__(self,ano,fabricante,modelo):
        """Método de definição de atributos"""
        self.ano = ano
        self.fabricante = fabricante
        self.modelo = modelo
        self.odometro = 0
        self.tanque = 0
    def apresentacao(self):
        """Método para descrição elegante do carro"""
        descricao = str(self.ano) + " " + self.fabricante.title() + " " + self.modelo.title()
        return descricao
    def leitura_odometro(self):
        """Método para apresentação do odômetro"""
        print("O odômetro do carro está marcando " + str(self.odometro) + 
              " Kilômetros rodados.")
    def alteracao_odometro(self,km):
        """Método para alteração do valor do odômetro"""
        if km >= self.odometro:
            self.odometro = km
        else:
            print("Não se pode diminuir o valor do odômetro.")
    def incremento_odometro(self,incremento):
        """Método para incrementar o valor do odômetro com uma quantia definida"""
        if incremento >= 0:
            self.odometro += incremento
        else:
            print("Não se pode diminuir o valor do odômetro.")
    def capacidade_tanque(self,tanque):
        """Método para informar o volume de combustível no tanque"""
        self.tanque = tanque
#meu_carro = Carro(2016,"Audi","A4")
#print(meu_carro.apresentacao())
#meu_carro.leitura_odometro()
#meu_carro.alteracao_odometro(60)
#meu_carro.leitura_odometro()
#meu_carro_velho = Carro(2012,"Honda","Civic")
#print(meu_carro_velho.apresentacao())
#meu_carro_velho.alteracao_odometro(57000)
#meu_carro_velho.leitura_odometro()
#meu_carro_velho.incremento_odometro(-100)
#meu_carro_velho.leitura_odometro()

#class Carro_Eletrico(Carro):
#    """Classe com características dos carros elétricos"""
#    def __init__(self,ano,fabricante,modelo):
#        """Método de inicialização"""
#        super().__init__(ano,fabricante,modelo)
#        self.bateria = 70
#    def capacidade_bateria(self):
#        """Método para informar a capacidade da bateria"""
#        print("Este carro tem uma bateria com " + str(self.bateria) + " -KWh.")
#    def capacidade_tanque(self):
#        """Carro elétrico não tem tanque de combustível"""
#        print("Carro elétrico não tem tanque de combustível.")
#carro_eletrico = Carro_Eletrico(2024,"Tesla","model")
#print(carro_eletrico.apresentacao())
#carro_eletrico.capacidade_bateria()
#carro_eletrico.capacidade_tanque()

class Bateria():
    """Classe que representa minimamente uma bateria"""
    def __init__(self,capacidade=70):
        self.capacidade = capacidade
    def capacidade_bateria(self):
        print("Este carro tem uma bateria com " + str(self.capacidade) + " -KWh")
    def autonomia(self):
        if self.capacidade == 70:
            auto = 240
        elif self.capacidade == 80:
            auto = 270
        mensagem = "Este carro consegue rodar aproximadamente " + str(auto)
        mensagem += " quilômetros com a beteria carregada."
        print(mensagem)
class Carro_Eletrico(Carro):
    """Classe com características dos carros elétricos"""
    def __init__(self,ano,fabricante,modelo):
        """Método de inicialização"""
        super().__init__(ano,fabricante,modelo)
        self.bateria = Bateria()
    def capacidade_tanque(self):
        """Carro elétrico não tem tanque de combustível"""
        print("Carro elétrico não tem tanque de combustível.")
novo_eletrico = Carro_Eletrico(2024,"BYD","Dolphin")
print(novo_eletrico.apresentacao())
novo_eletrico.bateria.capacidade_bateria()
novo_eletrico.bateria.autonomia()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
