def counting_sort(arr, place):
    counts = [0] * 10
    result = [0] * len(arr)

    for num in arr:
        index = int(num / place) % 10
        counts[index] += 1

    for i in range(1, 10):
        counts[i] += counts[i-1]

    i = len(arr) - 1
    while i >= 0:
        index = int(arr[i]/place) % 10
        result[counts[index]-1] = arr[i]
        counts[index] -= 1
        i -= 1

    return result


def radix_sort(arr):
    max_num = max(arr)
    place = 1
    while max_num > place:
        arr = counting_sort(arr, place)
        place += 10
    return arr


if __name__ == "__main__":
    import random
    arr = [random.randint(0, 1000) for _ in range(10)]
    arr = radix_sort(arr)
    for i in arr:
        print(i)
