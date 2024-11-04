def busca_binaria_iterativa(arr, x):
    left, right = 0, len(arr) - 1  
    while left <= right:
        mid = left + (right - left) // 2  
        if arr[mid] == x:
            return mid  
        elif arr[mid] < x: 
            left = mid + 1  
        else: 
            right = mid - 1  
    return -1 

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
x = 56
    
result = busca_binaria_iterativa(arr, x)
if result != -1:
    print(f"Elemento {x} foi encontrado no índice {result}")
else:
    print("Elemento não encontrado")
