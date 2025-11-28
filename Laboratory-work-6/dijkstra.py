import heapq

graph = {
    1: {3: 1, 2: 8, 4: 5, 5: 3},
    2: {1: 8, 3: 6, 5: 6, 6: 1},
    3: {1: 1, 2: 6, 6: 7, 8: 3},
    4: {1: 5, 5: 2},
    5: {1: 3, 2: 6, 4: 2, 7: 9},
    6: {2: 1, 3: 7, 7: 3, 8: 1},
    7: {5: 9, 6: 3, 8: 4},
    8: {3: 3, 6: 1, 7: 4}
}

def dijkstra(start):
    dist = {v: float('inf') for v in graph}
    pred = {v: None for v in graph}
    dist[start] = 0

    pq = [(0, start)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph[u].items():
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                pred[v] = u
                heapq.heappush(pq, (new_dist, v))
    return dist, pred

dist, pred = dijkstra(1)

print("Shortest distances:", dist)
print("Predecessors:", pred)
