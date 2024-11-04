def busca_binaria_recursiva(arr, x, left, right):
    if left > right:  
        return -1
    mid = left + (right - left) // 2 
    if arr[mid] == x: 
        return mid  
    elif arr[mid] < x: 
        return busca_binaria_recursiva(arr, x, mid + 1, right)  
    else: 
        return busca_binaria_recursiva(arr, x, left, mid - 1)  
    
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
x = 56

result = busca_binaria_recursiva(arr, x, 0, len(arr) - 1)

if result != -1:
    print(f"Elemento {x} foi encontrado no índice {result}")
else:
    print("Elemento não encontrado")
