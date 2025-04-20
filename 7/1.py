# 7-1
# Prim's Algorithm

import sys

input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(K)]

W = [[INF] * (N + 1) for _ in range(N + 1)]
for u, v, w in edges:
    W[u][v] = W[v][u] = w

distance = [INF] * (N + 1)
nearest = [0] * (N + 1)
mst = []  # (vnear, nearest[vnear], weight)


for v in range(2, N + 1):
    distance[v] = W[1][v]
    nearest[v] = 1

print(*nearest[2:])

for _ in range(N - 1):
    vnear = -1
    best = INF
    for v in range(2, N + 1):
        if 0 <= distance[v] < best:
            best = distance[v]
            vnear = v

    distance[vnear] = -1
    for v in range(2, N + 1):
        if distance[v] > W[vnear][v]:
            distance[v] = W[vnear][v]
            nearest[v] = vnear

    print(*nearest[2:])

    mst.append((vnear, nearest[vnear], W[vnear][nearest[vnear]]))

for vnear, p, c in mst:
    print(vnear, p, c)
