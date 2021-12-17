def quick_sort(arr):
    def _quick_sort(arr, low, high):
        if low < high:
            partition_index = partition(arr, low, high)
            _quick_sort(arr, low, partition_index-1)
            _quick_sort(arr, partition_index+1, high)

    _quick_sort(arr, 0, len(arr)-1)
    return arr


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


if __name__ == "__main__":
    import random
    arr = [random.randint(0, 1000) for _ in range(10)]
    arr = quick_sort(arr)
    for i in arr:
        print(i)
