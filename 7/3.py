# 7-3
# Dijkstra's Algorithm

import sys

input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())

W = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(K):
    u, v, w = map(int, input().split())
    W[u][v] = w

C = int(input())
T = [int(input()) for _ in range(C)]

length = [INF] * (N + 1)
touch = [1] * (N + 1)
F = []


for v in range(2, N + 1):
    length[v] = W[1][v]

print(*touch[2:])

for _ in range(N - 1):
    vnear = -1
    best = INF
    for v in range(2, N + 1):
        if 0 <= length[v] < best:
            best = length[v]
            vnear = v

    F.append((touch[vnear], vnear, W[touch[vnear]][vnear]))

    for v in range(2, N + 1):
        if length[v] > best + W[vnear][v]:
            length[v] = best + W[vnear][v]
            touch[v] = vnear

    print(*touch[2:])

    length[vnear] = -1

for u, v, w in F:
    print(u, v, w)

for t in T:
    path = []
    cur = t

    while cur != 1:
        path.append(cur)
        cur = touch[cur]

    path.append(1)
    path.reverse()

    print(*path)
