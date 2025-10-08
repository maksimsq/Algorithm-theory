def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(n - 1):
        min_index = i
        assignments += 1  # присвоєння min_index

        for j in range(i + 1, n):
            comparisons += 1  # порівняння
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1  # присвоєння min_index

        comparisons += 1  # перевірка для обміну
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3  # три присвоєння при обміні

    return arr, comparisons, assignments


# тестування
my_list = [53, 100, 44, 74, 53, 38, 82, 65, 28]
sorted_list, comps, assigs = selection_sort(my_list.copy())
print("Оригінальний список:", my_list)
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigs}")
