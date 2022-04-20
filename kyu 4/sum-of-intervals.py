def sum_of_intervals(intervals):
    intervalo = []
    for x in intervals:
        for y in range(x[0],x[1]):
            if y not in intervalo:
                intervalo.append(y)
    return len(intervalo)