import timeit
from quicksort import *

array = [-1, 0, 92, 91, 1923, 34, -9, 100, 0 , 2, 81]
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


choice = input('Какой вид сортировки?(1 - quicksort, 2 - расческой, 3 - блочная, 4 - пирамидальная): ')
if choice == '1':

    start_time = timeit.default_timer()
    quickSort(array, 0, len(array) - 1)
    time1 = timeit.default_timer() - start_time
    print(array)
    print('Время:', time1)

elif choice == '2':

    start_time = timeit.default_timer()
    combSort(array)
    time2 = timeit.default_timer() - start_time
    print(array)
    print('Время:', time2)

elif choice == '3':

    start_time = timeit.default_timer()
    bucketSort(array, 4)
    time3 = timeit.default_timer() - start_time
    print(array)
    print('Время:', time3)

elif choice == '4':

    start_time = timeit.default_timer()
    heapSort(array)
    time4 = timeit.default_timer() - start_time
    print(array)
    print('Время:', time4)

else:

    print('Неправильный ввод.')