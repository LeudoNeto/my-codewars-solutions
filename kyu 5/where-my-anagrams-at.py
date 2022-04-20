def anagrams(word, words):
    anagramas = []
    for x in words:
        anagrama = True
        for y in x:
            if x.count(y) != word.count(y):
                anagrama = False
        if anagrama:
            anagramas.append(x)
    return anagramas