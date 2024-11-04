import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))  
    prev = 0

    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  

    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1  

    if arr[prev] == x:
        return prev

    return -1  

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 6

result = jump_search(arr, x)

if result != -1:
    print(f'Elemento encontrado na posição: {result}')
else:
    print('Elemento não encontrado.')
