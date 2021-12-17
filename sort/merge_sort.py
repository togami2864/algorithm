def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    center = len(arr)//2
    left = arr[:center]
    right = arr[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


if __name__ == "__main__":
    import random
    arr = [random.randint(0, 1000) for _ in range(10)]
    arr = merge_sort(arr)
    for i in arr:
        print(i)
