import random
import time
import matplotlib.pyplot as plt

# ------------------------ АЛГОРИТМИ ------------------------

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def shell_sort(arr):
    arr = arr.copy()
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap //= 2

    return arr


def shell_hibbard(arr):
    arr = arr.copy()
    n = len(arr)

    gaps = []
    k = 1
    while (2 ** k - 1) <= n:
        gaps.append(2 ** k - 1)
        k += 1
    gaps.reverse()

    for gap in gaps:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key

    return arr


def shell_sedgewick(arr):
    arr = arr.copy()
    n = len(arr)
    gaps = []
    k = 0

    while True:
        g = 9 * (2 ** k) - 9 * (2 ** (k // 2)) + 1
        if g > n:
            break
        gaps.append(g)
        k += 1
    gaps.reverse()

    for gap in gaps:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key

    return arr


# ------------------------ Вимір часу ------------------------

def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    return time.time() - start


# ------------------------ Ввід користувача ------------------------

input_sizes = list(map(int, input("Введіть розміри масивів через кому (наприклад 1000,3000,5000): ").split(",")))
min_val = int(input("Мінімальне значення елемента: "))
max_val = int(input("Максимальне значення елемента: "))


# ------------------------ Порівняння алгоритмів ------------------------

def compare_algorithms():
    insertion_times = []
    shell_times = []
    hibb_times = []
    sedge_times = []

    for size in input_sizes:
        arr = [random.randint(min_val, max_val) for _ in range(size)]

        print("\n========================================")
        print(f"=== РОЗМІР МАСИВУ: {size} ===")
        print("Вхідний масив:")
        print(arr)

        # Копії
        arr1 = arr.copy()
        arr2 = arr.copy()
        arr3 = arr.copy()
        arr4 = arr.copy()

        # ВІДСОРТОВАНІ МАСИВИ
        s1 = insertion_sort(arr1)
        s2 = shell_sort(arr2)
        s3 = shell_hibbard(arr3)
        s4 = shell_sedgewick(arr4)

        print("\nВідсортовані масиви:")
        print("Insertion Sort:", s1)
        print("Shell classic:", s2)
        print("Hibbard:", s3)
        print("Sedgewick:", s4)

        # ЧАС
        t1 = measure_time(insertion_sort, arr.copy())
        t2 = measure_time(shell_sort, arr.copy())
        t3 = measure_time(shell_hibbard, arr.copy())
        t4 = measure_time(shell_sedgewick, arr.copy())

        insertion_times.append(t1)
        shell_times.append(t2)
        hibb_times.append(t3)
        sedge_times.append(t4)

        print("\nЧас виконання:")
        print(f"Insertion:  {t1:.6f} сек")
        print(f"Shell:      {t2:.6f} сек")
        print(f"Hibbard:    {t3:.6f} сек")
        print(f"Sedgewick:  {t4:.6f} сек")

    # ------------------------ Графік ------------------------
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, insertion_times, marker='o', label="Insertion Sort")
    plt.plot(input_sizes, shell_times, marker='o', label="Shell classic")
    plt.plot(input_sizes, hibb_times, marker='o', label="Hibbard Shell")
    plt.plot(input_sizes, sedge_times, marker='o', label="Sedgewick Shell")

    plt.title("Порівняння часу виконання алгоритмів сортування")
    plt.xlabel("Розмір масиву (кількість елементів)")
    plt.ylabel("Час (сек)")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    compare_algorithms()
