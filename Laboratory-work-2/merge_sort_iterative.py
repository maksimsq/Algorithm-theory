def merge_iterative(a, left, mid, right, temp, ops):
    i, j, k = left, mid, left
    while i < mid and j < right:
        ops["compare"] += 1
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        ops["assign"] += 1
        k += 1

    while i < mid:
        temp[k] = a[i]
        i += 1
        k += 1
        ops["assign"] += 1

    while j < right:
        temp[k] = a[j]
        j += 1
        k += 1
        ops["assign"] += 1

    for i in range(left, right):
        a[i] = temp[i]
        ops["assign"] += 1


def merge_sort_iterative(arr):
    n = len(arr)
    temp = arr.copy()
    ops = {"compare": 0, "assign": 0}

    size = 1
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            merge_iterative(arr, left, mid, right, temp, ops)
        size *= 2
    return arr, ops


if __name__ == "__main__":
    array = [53, 100, 44, 74, 53, 38, 82, 65, 28]
    print("Початковий масив:", array)
    sorted_arr, ops = merge_sort_iterative(array.copy())
    print("Відсортований масив:", sorted_arr)
    print("Кількість операцій:", ops)
