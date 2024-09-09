import random
 
class Cartas():
    valor_cartas = {
        'A' : 11,
        'K' : 10,
        'J' : 10,
        'Q' : 10,
        '10': 10,
        '9' : 9,
        '8' : 8,
        '7' : 7,
        '6' : 6,
        '5' : 5,
        '4' : 4,
        '2' : 2,
        '3' : 3
    }
 
    valor_naipes = {
        "♦" : 0,
        "♠" : 0,
        "♥" : 0,
        "♣" : 0
    }
 
 
    baralho = []    
 
    for naipe in valor_naipes:
        for carta in valor_cartas:
            baralho.append(naipe+carta)
 
   
 
 
class Valor_cartas():
   
   
    def valores(carta):
        naipe, valor = carta
        return Cartas.valor_naipes[naipe] + Cartas.valor_cartas[valor]
 
 
class Jogo():
    def __init__(self):
        self.jogador = []
        self.dealer = []
 
   
    def entregar_cartas(self):
        for i in range(2):
            r = random.choice(Cartas.baralho)
            self.jogador.append(r)
            Cartas.baralho.remove(r)
        for i in range(2):
            r = random.choice(Cartas.baralho)
            self.dealer.append(r)
            Cartas.baralho.remove(r)
     
    def get_mao_jogador(self):
        return self.jogador
    def get_mao_dealer(self):
        return self.dealer
   
    def sum_mao(self):
        valorj = sum(Valor_cartas.valores(carta) for carta in self.jogador)
        print(f'|A sua mão está em {valorj}|')
        valord = sum(Valor_cartas.valores(carta) for carta in self.dealer)
        print(f'|A mão do Dealer está em {valord}|')
 
    def sum_mao_jogador(self):
        valorj = sum(Valor_cartas.valores(carta) for carta in self.jogador)
        print(f'|A sua mão está em {valorj}|')
 
 
    def pedir_cartas(self):
        v = random.choice(Cartas.baralho)
        self.jogador.append(v)
        Cartas.baralho.remove(v)
 
    def carta_dealer(self):
        r = random.choice(Cartas.baralho)
        self.dealer.append(r)
        Cartas.baralho.remove(r)
 
    def permanecer(self):
        print('jogador permaneceu com a sua mão')
   
    #def verificar(self):
 
 
print('BLACKJACK')
 
 
j1 = Jogo()
 
j1.entregar_cartas()
print(f'Mão do Jogador {j1.get_mao_jogador()}')
print(f'Mão do Jogador {j1.get_mao_dealer()}')
j1.sum_mao()
 
print('Selecione a sua jogada de acordo com o numero.')
print('1. pedir cartas')
print('2. permanecer')
escolha = int(input())
 
 
 
 
if escolha == 1:
    j1.pedir_cartas()
    print(f'Mão do Jogador {j1.get_mao_jogador()}')
    j1.sum_mao_jogador()
else:
    j1.permanecer()
 