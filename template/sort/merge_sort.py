def merge_sort(arr):
    pass


if __name__ == "__main__":
    import random
    # arr = [5, 4, 1, 8, 7, 3, 2, 7]
    arr = [random.randint(0, 1000) for _ in range(10)]
    arr = merge_sort(arr)
    for i in arr:
        print(i)
