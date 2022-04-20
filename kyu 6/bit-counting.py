def count_bits(n):
    binario = bin(n)[2:]
    return binario.count('1')