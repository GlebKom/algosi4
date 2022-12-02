def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def combSort(array):
    step = int(len(array)/1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(array):
            if array[i] > array[i + step]:
                array[i], array[i + step] = array[i + step], array[i]
                swap += 1
            i = i + 1
        if step > 1:
            step = int(step / 1.247)

def bucketSort(array, n):
    buckets = []
    min_el = min(array)
    max_el = max(array)
    for i in range(n):
        buckets.append([])
    if min_el == max_el:
        return
    for element in array:
        buckets[(n * (element - min_el)) // (max_el - min_el + 1)].append(element)
    for bucket in buckets:
        if len(bucket) > 1:
            bucketSort(bucket, n)
    instert_index = 0
    for bucket in buckets:
        for element in bucket:
            array[instert_index] = element
            instert_index += 1

def heapify(array, heap_size, root_index):

    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and array[left_child] > array[largest]:
        largest = left_child

    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child

    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        heapify(array, heap_size, largest)

def heapSort(array):
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)