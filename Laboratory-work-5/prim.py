# Алгоритм Пріма для пошуку мінімального кістякового дерева (МКД)
# Вага графа зображена в adjacency list

import heapq

graph = {
    1: {2:8, 3:1, 4:5, 5:3},
    2: {1:8, 4:6, 5:6, 6:1},
    3: {1:1, 4:6, 6:7, 8:3},
    4: {1:5, 2:6, 3:6, 5:2},
    5: {1:3, 2:6, 4:2, 7:9},
    6: {2:1, 3:7, 7:3, 8:1},
    7: {5:9, 6:3, 8:4},
    8: {3:3, 6:1, 7:4}
}

def prim(graph, start=1):
    visited = set()
    mst = []  # ребра МКД
    pq = []   # мін-heap

    visited.add(start)

    # Додаємо усі ребра зі стартової вершини
    for neigh, w in graph[start].items():
        heapq.heappush(pq, (w, start, neigh))

    while pq:
        w, u, v = heapq.heappop(pq)

        if v in visited:
            continue

        mst.append((u, v, w))
        visited.add(v)

        for neigh, ww in graph[v].items():
            if neigh not in visited:
                heapq.heappush(pq, (ww, v, neigh))

    return mst

mst = prim(graph, 1)

print("МКД (алгоритм Пріма):")
for edge in mst:
    print(edge)

print("\nСума ваг:", sum([w for _,_,w in mst]))
