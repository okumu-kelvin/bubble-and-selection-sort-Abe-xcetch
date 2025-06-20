def bubble_sort(arr):
    # TODO: Implement bubble sort
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

data = [5,4,7,9,8]
data.reverse()
print("Reversed:", data)
bubble_sort(data)
print("Sorted:", data)