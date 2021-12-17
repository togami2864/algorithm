def heapify(arr, i):
    left = 2*i + 1
    right = 2*i + 2
    length = len(arr) - 1
    biggest = i

    if left <= length and arr[biggest] < arr[left]:
        biggest = left
    if right <= length and arr[biggest] < arr[right]:
        biggest = right
    if biggest != i:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        heapify(arr, biggest)


def build_heap(arr):
    for i in reversed(range(len(arr)//2)):
        heapify(arr, i)
    return arr


def heap_sort(arr):
    arr = build_heap(arr)
    sorted_array = []
    for _ in range(len(arr)):
        arr[0], arr[-1] = arr[-1], arr[0]
        sorted_array.append(arr.pop())
        heapify(arr, 0)
    return sorted_array


if __name__ == '__main__':
    array = [1, 9, 8, 2, 3, 10, 14, 7, 16, 4]
    array = heap_sort(array)
    for i in array:
        print(i)
