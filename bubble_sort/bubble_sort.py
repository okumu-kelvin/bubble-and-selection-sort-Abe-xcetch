def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    n = len(unsorted_list)

    for i in range(n):
        for j in range(0, n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]


    data = [5,3,6,8,9]
    bubble_sort(data)
    print("Bubble sorted: ", data)
    pass
