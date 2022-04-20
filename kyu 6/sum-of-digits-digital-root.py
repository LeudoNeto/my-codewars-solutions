def digital_root(n):
    while True:
        m = str(n)
        if len(m) > 1:
            soma = 0
            for x in m:
                soma = soma + int(x)
            n = soma
        else:
            break
    return n