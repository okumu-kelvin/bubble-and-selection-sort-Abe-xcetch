def selection_sort(arr):
    # TODO: Implement selection sort
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
data = [5,3,6,8,9]
selection_sort(data)
print("Selection sorted: ", data)


