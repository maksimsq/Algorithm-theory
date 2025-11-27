# Вершини графа
V = {1, 2, 3, 4, 5, 6, 7, 8}

# (вага, вершина1, вершина2)
edges = [
    (1, 1, 3),
    (1, 2, 6),
    (1, 6, 8),
    (2, 4, 5),
    (3, 1, 5),
    (3, 3, 8),
    (3, 6, 7),
    (4, 7, 8),
    (5, 1, 4),
    (6, 2, 4),
    (6, 2, 5),
    (6, 3, 4),
    (7, 3, 6),
    (8, 1, 2),
    (9, 5, 7),
]

# Union-Find (роздільна система множин)
parent = {v: v for v in V}
rank = {v: 0 for v in V}


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    ra, rb = find(a), find(b)

    if ra == rb:
        return False

    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True


# === Алгоритм Крускала ===
edges.sort()

mst = []  # результат МКД

print("=== Кроки алгоритму Крускала ===")
for w, u, v in edges:
    if union(u, v):
        mst.append((u, v, w))
        print(f"Додано ребро ({u}–{v}) з вагою {w}")

print("\n=== Результат МКД ===")
total = sum(w for _, _, w in mst)
for u, v, w in mst:
    print(f"{u} — {v} : {w}")
print(f"\nЗагальна вага: {total}")
