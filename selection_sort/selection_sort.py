def selection_sort(arr):
    # TODO: Implement selection sort
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
data = [5,4,7,9,8]
data.reverse()
print("Reversed:", data)
selection_sort(data)
print("Sorted:", data)


