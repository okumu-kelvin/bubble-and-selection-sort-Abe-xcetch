def bubble_sort(arr):
    # TODO: Implement bubble sort
    if has_duplicates(arr):
        print("Duplicates")
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def has_duplicates(arr):
    return len(arr) != len(set(arr))


