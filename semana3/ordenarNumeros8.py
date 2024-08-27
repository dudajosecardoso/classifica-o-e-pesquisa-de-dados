def shellSort(arr):
    count = len(arr) // 2
    while count > 0:
        for posInicial in range(count):
            puloInsertionSort(arr, posInicial, count)
        count = count // 2
    return arr

def puloInsertionSort(arr, start, pulo):
    for i in range(start + pulo, len(arr), pulo):
        valor = arr[i]
        j = i
        while j >= pulo and arr[j - pulo] > valor:
            arr[j] = arr[j - pulo]
            j -= pulo
            arr[j] = valor
    return arr


arr = [12, 34, 54, 2, 3]
print(arr)
print(shellSort(arr))
