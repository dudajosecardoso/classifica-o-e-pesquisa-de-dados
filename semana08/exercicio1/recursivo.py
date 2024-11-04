def busca_binaria_recursiva(arr, buscado, left, right):
    if left > right:  
        return -1
    mid = left + (right - left) // 2 
    if arr[mid] == buscado: 
        return mid  
    elif arr[mid] < buscado: 
        return busca_binaria_recursiva(arr, buscado, mid + 1, right)  
    else: 
        return busca_binaria_recursiva(arr, buscado, left, mid - 1)  
    
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
buscado = 56

result = busca_binaria_recursiva(arr, buscado, 0, len(arr) - 1)

if result != -1:
    print(f"Elemento {buscado} foi encontrado no índice {result}")
else:
    print("Elemento não encontrado")
