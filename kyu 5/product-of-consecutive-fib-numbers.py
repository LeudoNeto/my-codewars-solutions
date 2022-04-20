def productFib(prod):
    condicao = False
    passou = False
    sequencia = [1,1]
    a = 1
    b = 1
    if prod == 0:
        return [0,1,True]
    while True:
        a = a + b
        b = a - b
        sequencia.append(a)
        if len(sequencia) ==1000:
            break
    for x in range(0,len(sequencia)-1):
        if prod == (sequencia[x]*sequencia[x+1]):
            condicao = True
            if condicao:
                f1 = sequencia[x]
                f2 = sequencia[x+1]
                passou = True
        if prod < (sequencia[x]*sequencia[x+1]) and not passou:
            passou = True
            f1 = sequencia[x]
            f2 = sequencia[x+1]
    return [f1,f2,condicao]