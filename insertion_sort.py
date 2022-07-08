def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if (arr[j+1] < arr[j]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
            else:
                break
    return arr


arr = [7, 4, 3, 6, 9, 5, 8, 2, 10, 1]

print(f'Before: {arr}')
print(f'After: {insertion_sort(arr)}')
