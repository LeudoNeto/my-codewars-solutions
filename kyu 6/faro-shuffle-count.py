def faro_cycles(ds):
    i = 0
    baralho = list(range(0,ds))
    atual = baralho
    while atual != baralho or i == 0:
        novo = []
        for x in atual[::2]:
            novo.append(x)
        for x in atual[1::2]:
            novo.append(x)
        i = i + 1
        atual = novo
    return i