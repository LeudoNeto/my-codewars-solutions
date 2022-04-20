def narcissistic( value ):
    n = str(value)
    soma = 0
    for x in n:
        soma = soma + int(x)**len(n)
    if value == soma:
        return True
    else:
        return False