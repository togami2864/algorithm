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


def bucket_sort(arr):
    max_num = max(arr)
    length = len(arr)
    size = max_num // length

    buckets = [[] for _ in range(size)]
    for num in arr:
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[size-1].append(num)

    for i in range(size):
        insertion_sort(buckets[i])

    result = []
    for i in range(size):
        result += buckets[i]

    return result


if __name__ == "__main__":
    import random
    arr = [random.randint(0, 1000) for _ in range(10)]
    arr = bucket_sort(arr)
    for i in arr:
        print(i)
