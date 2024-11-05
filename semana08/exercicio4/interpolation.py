def pesqInterpolacao(array, x):
    esq = 0
    dir = len(array) - 1

    while esq <= dir and x >= array[esq] and x <= array[dir]:
        pos = esq + ((dir - esq) // (array[dir] - array[esq]) * (x - array[esq]))

        if array[pos] == x:
            return pos
        elif array[pos] < x:
            esq = pos + 1
        else:
            dir = pos - 1

    return -1

array = [1, 10, 11, 14, 16, 20]
x = 20
ind = pesqInterpolacao(array, x)
print(ind)
