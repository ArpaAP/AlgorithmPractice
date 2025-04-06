# 5-3
# Floyd Algorithm

import sys

input = sys.stdin.readline

INF = 999

N, M = map(int, input().split())

W = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())

    W[u][v] = w

    W[u][u] = 0
    W[v][v] = 0

K = int(input())

L = [tuple(map(int, input().split())) for _ in range(K)]

D = [r[:] for r in W]
P = [[0] * (N + 1) for _ in range(N + 1)]

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]
                P[i][j] = k


def path(u, v):
    p = []

    def inner(u, v):
        k = P[u][v]
        if k == 0:
            return

        inner(u, k)
        p.append(k)
        inner(k, v)

    inner(u, v)

    return p


def print_matrix(m):
    for row in m[1:]:
        print(*row[1:])


print_matrix(D)
print_matrix(P)

for u, v in L:
    p = path(u, v)
    if p:
        print(u, *p, v)
    elif W[u][v] < INF:
        print(u, v)
    else:
        print("NONE")
