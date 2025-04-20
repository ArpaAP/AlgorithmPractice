# 7-2
# Kruskal's Algorithm

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(K)]
edges.sort(key=lambda x: x[2])

parent = list(range(N + 1))

F = []


def find_parent(i):
    while parent[i] != i:
        i = parent[i]

    return i


def merge(u, v):
    u = find_parent(u)
    v = find_parent(v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v


for e in edges:
    u, v, w = e

    if find_parent(u) != find_parent(v):
        merge(u, v)

        F.append(e)

for e in F:
    print(*e)
