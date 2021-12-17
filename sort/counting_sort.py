# require Memory
def counting_sort(arr):
    max_num = max(arr)
    counts = [0] * (max_num + 1)
    result = [0] * len(arr)

    for num in arr:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    i = len(arr) - 1
    while i >= 0:
        index = arr[i]
        result[counts[index]-1] = arr[i]
        counts[index] -= 1
        i -= 1
    return result


if __name__ == "__main__":
    import random
    arr = [random.randint(0, 1000) for _ in range(10)]
    arr = counting_sort(arr)
    for i in arr:
        print(i)
