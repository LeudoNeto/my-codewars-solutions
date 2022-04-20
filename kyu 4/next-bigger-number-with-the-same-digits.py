def next_bigger(n):
    n = str(n)
    quantos = {}
    possivel = False
    for x in range(0,len(n)-1):
        if n[x+1] > n[x]:
            possivel = True
    if not possivel:
        return -1
    for x in n:
        if f'{x}' not in quantos.keys():
            quantos[f'{x}'] = 1
        else:
            quantos[f'{x}'] += 1
    m = int(n)
    while True:
        quantosm = {}
        m += 1
        m = str(m)
        for x in m:
            if f'{x}' not in quantosm.keys():
                quantosm[f'{x}'] = 1
            else:
                quantosm[f'{x}'] += 1
            if quantosm == quantos:
                return int(m)
            m = int(m)