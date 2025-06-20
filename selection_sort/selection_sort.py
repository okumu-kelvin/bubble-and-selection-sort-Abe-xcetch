from bubble_sort.bubble_sort import has_duplicates


def selection_sort(arr):
    # TODO: Implement selection sort
    if has_duplicates(arr):
        print("Duplicates")
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]
def has_duplicates(arr):
    return len(arr) != len(set(arr))



