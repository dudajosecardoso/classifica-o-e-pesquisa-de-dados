import time 
import random

def medir_tempo(algoritmo, array):
    inicio = time.time()
    algoritmo(array)
    fim = time.time()
    return fim - inicio

def insertionSort(array):
    n = len(array)
    for i in range(1,n):
        key = array[i] 
        j = i-1 
        while j>=0 and key<array[j]:  
            array[j+1] = array[j] 
            j = j-1 
        array[j+1] = key 


def selectionSort(array):
    n = len(array)
    for i in range(n-1):
        menor = array[i]
        menor_id = i
        for j in range(i+1,n):
            if array[j] < menor:
                menor = array[j]
                menor_id = j
        array[i], array[menor_id] = array[menor_id], array[i]
    return array

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array



def shellSort(array):
    count = len(array) // 2
    while count > 0:
        for posInicial in range(count):
            puloInsertionSort(array, posInicial, count)
        print("Depois do incremento do tamanho",count,"a lista é ", array)
        count = count // 2
    return array

def puloInsertionSort(array, start, pulo):
    for i in range(start + pulo, len(array), pulo):
        valor = array[i]
        j = i
        while j >= pulo and array[j - pulo] > valor:
            array[j] = array[j - pulo]
            j -= pulo
            array[j] = valor
    return array

def mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quickSort(array, inicio, fim):
    if fim - inicio <= 1:  
        return
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



#array = sorted(random.sample(range(1, 10001), 1000)) #aleatorios ordenados #a
#array = sorted(random.sample(range(1, 10001), 1000), reverse=True) #aleatorios ordenados ao contrario #b
array =  random.sample(range(1000*2), 1000) #aleatorios sem elementos repetidos #d
#array = [random.randint(1, 10001) for _ in range(1000)] # aleatorios com elementos repetidos #c
n = len(array)
quickSort(array, 0, n - 1)

tempo_insertion_sort = medir_tempo(insertionSort, array.copy())
tempo_selection_sort = medir_tempo(selectionSort, array.copy())
tempo_bubble_sort = medir_tempo(bubbleSort, array.copy())
tempo_shell_sort = medir_tempo(shellSort, array.copy())
tempo_merge_sort = medir_tempo(mergeSort, array.copy())
tempo_quick_sort = medir_tempo(lambda x: quickSort(x, 0, len(x) - 1), array.copy())

print(f"Tempo de resposta do Insertion Sort: {tempo_insertion_sort:.6f} segundos")
print(f"Tempo de resposta do Selection Sort: {tempo_selection_sort:.6f} segundos")
print(f"Tempo de resposta do Bubble Sort: {tempo_bubble_sort:.6f} segundos")
print(f"Tempo de resposta do Shell Sort: {tempo_shell_sort:.6f} segundos")
print(f"Tempo de resposta do Merge Sort: {tempo_merge_sort:.6f} segundos")
print(f"Tempo de resposta do Quick Sort: {tempo_merge_sort:.6f} segundos")
