def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    arr = [3, 1, 7, 4, 8, 5, 4, 3, 1, 9, 13, 34, 43, 32, 5, 7]
    arr = bubble_sort(arr)
    for i in arr:
        print(i)
