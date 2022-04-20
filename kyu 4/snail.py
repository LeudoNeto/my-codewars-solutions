def snail(snail_map):
    tamanho = len(snail_map)**2
    saida = []
    x = 0
    y = 0
    while len(saida) < tamanho:
        while x < len(snail_map[0]):
            saida.append(snail_map[y][x])
            x = x + 1
        if x == len(snail_map[0]):
            snail_map.pop(y)
            x = x - 1
            if len(snail_map) == 0:
                return saida
        while y < len(snail_map):
            saida.append(snail_map[y][x])
            y = y + 1
        if y == len(snail_map):
            for z in snail_map:
                z.pop(x)
            y = y - 1
            x = x - 1
            if len(snail_map) == 0:
                return saida
        while x >= 0:
            saida.append(snail_map[y][x])
            x = x - 1
        if x == -1:
            snail_map.pop(y)
            x = 0
            y = y - 1
            if len(snail_map) == 0:
                return saida
        while y >= 0:
            saida.append(snail_map[y][x])
            y = y - 1
        if y == -1:
            for z in snail_map:
                z.pop(x)
            y = 0
            if len(snail_map) == 0:
                return saida