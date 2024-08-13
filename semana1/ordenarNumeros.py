def insertionSort(data,n):
    for i in range(1,n):
        key = data[i]
        j = i-1
        while j>=0 and key<data[j]:
            data[j+1] = data[j]
            j = j-1
        data[j+1] = key
    return data 

print(insertionSort([12,11,13,5,6,6],6))
