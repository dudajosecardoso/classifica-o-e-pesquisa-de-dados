def busca_binaria_iterativa(arr, buscado):
    left, right = 0, len(arr) - 1  
    while left <= right:
        mid = left + (right - left) // 2  
        if arr[mid] == buscado:
            return mid  
        elif arr[mid] < buscado: 
            left = mid + 1  
        else: 
            right = mid - 1  
    return -1 

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
buscado = 56
    
result = busca_binaria_iterativa(arr, buscado)
if result != -1:
    print(f"Elemento {buscado} foi encontrado no índice {result}")
else:
    print("Elemento não encontrado")
