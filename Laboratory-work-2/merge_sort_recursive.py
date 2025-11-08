def merge_recursive(left, right, ops):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        ops["compare"] += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        ops["assign"] += 1

    while i < len(left):
        result.append(left[i])
        i += 1
        ops["assign"] += 1

    while j < len(right):
        result.append(right[j])
        j += 1
        ops["assign"] += 1

    return result, ops


def merge_sort_recursive(arr, ops=None):
    if ops is None:
        ops = {"compare": 0, "assign": 0}

    if len(arr) <= 1:
        return arr, ops

    mid = len(arr) // 2
    left, ops = merge_sort_recursive(arr[:mid], ops)
    right, ops = merge_sort_recursive(arr[mid:], ops)
    merged, ops = merge_recursive(left, right, ops)
    return merged, ops


if __name__ == "__main__":
    array = [53, 100, 44, 74, 53, 38, 82, 65, 28]
    print("Початковий масив:", array)
    sorted_arr, ops = merge_sort_recursive(array.copy())
    print("Відсортований масив:", sorted_arr)
    print("Кількість операцій:", ops)
