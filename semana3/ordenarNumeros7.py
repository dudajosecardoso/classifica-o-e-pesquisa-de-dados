def quickSort(array, inicio, fim):
    n = len(array)
    if fim > inicio:
        pivo = particiona(array, inicio, fim)
        quickSort(array, inicio, pivo - 1)
        quickSort(array, pivo + 1, fim)

def particiona(array, inicio, final):
    esq = inicio
    dir = final
    pivo = array[inicio]
    while esq < dir:
        while esq <= final and array[esq] <= pivo:
            esq += 1
        while dir >= 0 and array[dir] > pivo:
            dir -= 1
        if esq < dir:
            array[esq], array[dir] = array[dir], array[esq]
    array[inicio], array[dir] = array[dir], pivo
    return dir

# Exemplo de uso
array = [5, 2, 8, 3, 1, 6, 4]
n = len(array)
quickSort(array, 0, n - 1)
print(array)  
