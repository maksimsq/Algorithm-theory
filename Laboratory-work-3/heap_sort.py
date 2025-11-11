def heap_sort(a):
    n = len(a)

    # просіювання вниз (sink) для max-heap
    def sink(i, size):
        while True:
            l = 2*i + 1
            r = 2*i + 2
            largest = i
            if l < size and a[l] > a[largest]:
                largest = l
            if r < size and a[r] > a[largest]:
                largest = r
            if largest == i:
                break
            a[i], a[largest] = a[largest], a[i]  # своп
            i = largest

    # 1) побудова максимальної купи
    for i in range(n//2 - 1, -1, -1):
        sink(i, n)

    # 2) власне сортування: максимум ↔ кінець, потім просіювання
    for end in range(n-1, 0, -1):
        a[0], a[end] = a[end], a[0]  # перенесення максимуму в кінець
        sink(0, end)                 # просіювання кореня у зменшеній купі

    return a

# приклад з твоєї послідовності
arr = [53, 100, 44, 74, 53, 38, 82, 65, 28]
print("Початково:", arr)
print("Відсортовано:", heap_sort(arr))
