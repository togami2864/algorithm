def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


if __name__ == "__main__":
    arr = [3, 1, 7, 4, 8, 5, 4, 3, 1, 9, 13, 34, 43, 32, 5, 7]
    arr = insertion_sort(arr)
    for i in arr:
        print(i)
