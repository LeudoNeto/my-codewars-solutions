def cakes(recipe, available):
    m = 9999
    for x in recipe.keys():
        print(x)
        if x not in available.keys():
            m = 0
        else:
            n = int(available[x]/recipe[x])
            print(n)
            if n < m:
                m = n
    return m