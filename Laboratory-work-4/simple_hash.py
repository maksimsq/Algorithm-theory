# Константа розміру таблиці
M = 13

# Список вхідних слів
WORDS = [
    "ХТО", "ДРІБНИМ", "НЕ", "РАДІЄ",
    "ТОЙ", "ВЕЛИКОГО", "НЕ", "ДОЧЕКАЄТЬСЯ"
]

# Український алфавіт з позиціями
LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8,
    'Ж': 9, 'З': 10, 'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15,
    'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20, 'Р': 21, 'С': 22,
    'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28, 'Ш': 29,
    'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}


def simple_hash_from_map(key: str) -> int:
    sum_of_positions = 0

    # Додаємо значення кожної букви слова
    for char in key:
        position = LETTER_POSITIONS.get(char.upper(), 0)
        sum_of_positions += position

    # Фінальна адреса
    hash_address = sum_of_positions % M
    return hash_address


def build_open_hash_table(words: list, m: int) -> list:
    # Ініціалізація таблиці: m порожніх списків
    hash_table = [[] for _ in range(m)]

    # Для кожного слова обчислюємо адресу і додаємо в ланцюжок
    for word in words:
        address = simple_hash_from_map(word)
        hash_table[address].append(word)

    return hash_table


def display_hash_table(table: list):
    print("\n--- Результат хешування (Таблиця M=13) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")


# Виконання алгоритму
hash_table = build_open_hash_table(WORDS, M)
display_hash_table(hash_table)
