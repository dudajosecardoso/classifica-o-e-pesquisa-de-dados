def countingSort(arr):
    max_val = max(arr)
    min_val = min(arr)
    count_arr = [0] * (max_val - min_val + 1)

    for num in arr:
        count_arr[num - min_val] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    output_arr = [0] * len(arr)
    for num in arr:
        output_arr[count_arr[num - min_val] - 1] = num
        count_arr[num - min_val] -= 1

    return output_arr

arr = [4, 2, 2, 8, 3, 3, 1]
arr = countingSort(arr)
print(arr)
