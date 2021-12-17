import heapq

# heapq.heapify --- build_heap
# heapq.heappop --- 要素入れ替え、末尾削除、min_heapify


def heap_sort(array):
    heapq.heapify(array)
    return [heapq.heappop(array) for _ in range(len(array))]


if __name__ == '__main__':
    array = [1, 9, 8, 2, 3, 10, 14, 7, 16, 4]
    array = heap_sort(array)
    for i in array:
        print(i)
