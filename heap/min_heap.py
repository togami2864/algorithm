def heapify_min(arr, i):
    left_index = 2*i + 1
    right_index = 2*i + 2
    smallest = i
    length = len(arr) - 1

    if left_index <= length and arr[i] > arr[left_index]:
        smallest = left_index
    if right_index <= length and arr[smallest] > arr[right_index]:
        smallest = right_index
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_min(arr, smallest)


def build_heap(arr):
    for i in reversed(range(len(arr)//2)):
        heapify_min(arr, i)
    return arr


def heap_sort(array):
    build_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        heapify_min(array, 0)
    return sorted_array


if __name__ == '__main__':
    array = [1, 9, 8, 2, 3, 10, 14, 7, 16, 4]
    array = heap_sort(array)
    for i in array:
        print(i)
    # sorted_array = build_heap(array)
    # for i in sorted_array:
    #     print(i)
