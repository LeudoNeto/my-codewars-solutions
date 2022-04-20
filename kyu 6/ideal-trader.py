class Trader:
    def __init__(self,amount):
        self.amount = amount

    def comprar(self,a):
        self.compra = a
        self.acoes = self.amount
        self.amount = 0

    def vender(self,a):
        self.amount = (a/self.compra)*self.acoes
        self.compra = 0
        self.acoes = 0

def ideal_trader(prices):
    altas = []
    baixas = []
    menor = 9999
    maior = 0
    a = 0
    while len(prices) > 0:
        if prices[a] > maior:
            maior = prices[a]
        if prices[a] < menor:
            menor = prices[a]
        a += 1
        if a < len(prices):
            if prices[a] < prices[a-1]:
                altas.append(maior)
                baixas.append(menor)
                del prices[:a]
                a = 0
                menor = 9999
                maior = 0
        else:
            altas.append(maior)
            baixas.append(menor)
            del prices[:a]
            a = 0
            menor = 9999
            maior = 0
    for x in range(0,len(baixas)):
        trader.comprar(baixas[x])
        trader.vender(altas[x])
    resposta = trader.amount
    trader.amount = 1
    return resposta

trader = Trader(1)