def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min_idx = i
        for j in range(i, length):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    arr = [3, 1, 7, 4, 8, 5, 4, 3, 1, 9, 13, 34, 43, 32, 5, 7]
    arr = selection_sort(arr)
    for i in arr:
        print(i)
