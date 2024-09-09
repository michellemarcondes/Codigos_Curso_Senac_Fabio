import random
 
class Cartas:
 
    naipe =['\u2660','\u2665','\u2666','\u2663']
    valor = ['A',2,3,4,5,6,7,8,9,10,'Q','J','R']
 
    def __init__(self, valor, naipe):
        self._valor = valor
        self._naipe = naipe
 
 
    def valor_cartas(self):
        if self.valor in ['J', 'Q', 'K']:
            return 10
        elif self.valor == 'A':
            return 11
        else:
            return int(self.valor)
 
 
    def __repr__(self):
        return f"{self._naipe}{self._valor}"
   
class Jogador:
 
    def __init__(self, nome):
        self._nome = nome
        self._rodada = Rodada()
        self._saturado = False
 
   
    def tirar(self, baralho):
        carta =  baralho.tirar()
        self._rodada.pedir_cartas(carta)
 
    def parar(self):
        self._saturado = True
 
class Jogo:
 
    def __init__(self, numero_jogadores=4):
        self.baralho = Baralho()
        self.jogadores = [Jogador(f"jogador {i+1}") for i in range(numero_jogadores)]
        self.dealer = Jogador("Dealer")

    def distribuicao_inicial(self):
        print("Distribuindo cartas iniciais...\n")
        for _ in range(2):
            for jogador in self.jogadores:
                jogador.tirar(self.baralho)
            self.dealer.tirar(self.baralho)

       
 
class Baralho ():
   
    def __init__(self):
        self._cartas = [Cartas(n,v) for n in Cartas.naipe for v in Cartas.valor]
 
 
    def embaralhar(self):
        return random.shuffle(self._cartas)
   
 
    def exibir(self):
        return self._cartas
   
class Rodada:
   
    def __init__(self):
        self._cartas = []
 
 
    def pedir_cartas(self, carta):
        self._cartas.append(carta)
 
   
    def calcula(self):
        valor = sum(carta.valor_cartas() for carta in self._cartas)
       
        num_ases = sum(1 for carta in self._cartas if carta.valor == 'A')
 
        while valor > 21 and num_ases:
            valor -= 10
            num_ases -= 1
            return valor
        
    def __repr__(self):
        return f'Rodada: {",".join(map(str, self._cartas))} {self.calcula()}'
 
baralho = Baralho()  