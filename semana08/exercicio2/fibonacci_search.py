def fibonacci_search(arr, x):
    n = len(arr)
    
    fib_m2 = 0  
    fib_m1 = 1  
    fib_m = fib_m2 + fib_m1  

    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1  

    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)

        if arr[i] < x:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i

        elif arr[i] > x:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i

    if fib_m1 and arr[offset + 1] == x:
        return offset + 1

    return -1

arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
x = 85

result = fibonacci_search(arr, x)

if result != -1:
    print(f'Elemento encontrado na posição: {result}')
else:
    print('Elemento não encontrado.')
