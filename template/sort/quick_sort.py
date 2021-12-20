def quick_sort(arr):
    pass


def partition(arr, low, high):
    pass


if __name__ == "__main__":
    import random
    arr = [random.randint(0, 1000) for _ in range(10)]
    arr = quick_sort(arr)
    for i in arr:
        print(i)
