def selectionSort(data):
    n = len(data)
    for i in range(n-1):
        menor = data[i]
        menor_id = i
        for j in range(i+1,n):
            if data[j] < menor:
                menor = data[j]
                menor_id = j
        data[i], data[menor_id] = data[menor_id], data[i]
    return data

lista= [64, 34, 25, 12, 22, 11, 90]
print("lista desordenada:", lista)
print("lista ordenada:", (selectionSort(lista))) 
