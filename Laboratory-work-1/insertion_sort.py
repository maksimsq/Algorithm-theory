def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    # проходимо по кожному елементу починаючи з другого
    for i in range(1, n):
        key = arr[i]
        assignments += 1
        j = i - 1
        assignments += 1

        # порівнюємо ключ з попередніми елементами і зсуваємо більші вправо
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1

        # додаткове порівняння, коли цикл зупинився не через межі
        if j >= 0:
            comparisons += 1

        # вставляємо ключ у потрібне місце
        arr[j + 1] = key
        assignments += 1

    # повертаємо відсортований масив і статистику
    return arr, comparisons, assignments


# тестування
my_list = [53, 100, 44, 74, 53, 38, 82, 65, 28]
sorted_list, comps, assigs = insertion_sort(my_list.copy())
print("Оригінальний список:", my_list)
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigs}")
