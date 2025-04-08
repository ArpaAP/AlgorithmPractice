# 6-1
# Chained Matrix Multiplication

import sys

N = int(input())
d = list(map(int, input().split()))

M = [[0] * (N + 1) for _ in range(N + 1)]
P = [[0] * (N + 1) for _ in range(N + 1)]


def minimum(i, j, d, M):
    min_value = sys.maxsize

    for k in range(i, j):
        value = M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]
        if min_value > value:
            min_value = value
            min_k = k

    return min_value, min_k


def minmult(n, d, M, P):
    for diag in range(1, n):
        for i in range(1, n - diag + 1):
            j = i + diag
            M[i][j], k = minimum(i, j, d, M)
            P[i][j] = k

    return M[1][n]


def order(i, j, P):
    s = ""

    def inner(i, j):
        nonlocal s

        if i == j:
            s += f"(A{i})"
        else:
            k = P[i][j]
            s += "("
            inner(i, k)
            inner(k + 1, j)
            s += ")"

    inner(i, j)

    return s


def print_diagonal(M):
    for i, row in enumerate(M[1:], 1):
        print(*row[i:])


v = minmult(N, d, M, P)


print_diagonal(M)
print_diagonal(P)

print(v)
print(order(1, N, P))
