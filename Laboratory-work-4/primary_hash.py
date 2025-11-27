# Константа розміру таблиці
M = 13

# Список вхідних слів
WORDS = ["ХТО", "ДРІБНИМ", "НЕ", "РАДІЄ",
         "ТОЙ", "ВЕЛИКОГО", "НЕ", "ДОЧЕКАЄТЬСЯ"]

# Словник позицій українського алфавіту (1–33)
LETTER_POSITIONS = {
'А':1,'Б':2,'В':3,'Г':4,'Ґ':5,'Д':6,'Е':7,'Є':8,'Ж':9,'З':10,'И':11,'І':12,'Ї':13,'Й':14,
'К':15,'Л':16,'М':17,'Н':18,'О':19,'П':20,'Р':21,'С':22,'Т':23,'У':24,'Ф':25,'Х':26,'Ц':27,
'Ч':28,'Ш':29,'Щ':30,'Ь':31,'Ю':32,'Я':33
}

def primary_hash(key: str) -> int:
    total = 0
    for char in key:
        total += LETTER_POSITIONS.get(char.upper(), 0)
    return total % M


def build_closed_hash_table(words: list, m: int) -> list:
    table = [None] * m

    for word in words:
        start = primary_hash(word)

        for i in range(m):
            idx = (start + i) % m
            if table[idx] is None:
                table[idx] = word
                break
        else:
            print(f"Помилка!!! Таблиця повна! Не вставлено: {word}")

    return table


def display_hash_table(table: list):
    print("\n--- Хеш-таблиця (Відкрита адресація, M=13) ---")
    print("Індекс | Слово")
    print("-------|-------------------")
    for i, v in enumerate(table):
        print(f"{i:02d} | {v if v else '(NULL)'}")


# Виконання
hash_table = build_closed_hash_table(WORDS, M)
display_hash_table(hash_table)
