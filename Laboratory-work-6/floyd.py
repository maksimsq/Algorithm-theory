INF = float('inf')

W = [
    [0, 8, 1, 5, 3, INF, INF, INF],
    [8, 0, 6, INF, 6, 1, INF, INF],
    [1, 6, 0, INF, INF, 7, INF, 3],
    [5, INF, INF, 0, 2, INF, INF, INF],
    [3, 6, INF, 2, 0, INF, 9, INF],
    [INF, 1, 7, INF, INF, 0, 3, 1],
    [INF, INF, INF, INF, 9, 3, 0, 4],
    [INF, INF, 3, INF, INF, 1, 4, 0]
]

n = len(W)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if W[i][k] + W[k][j] < W[i][j]:
                W[i][j] = W[i][k] + W[k][j]

for row in W:
    print(row)
