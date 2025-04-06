# 5-5
# Triangle Path (2): Find Optimal Solution

C = int(input())

cache = []


def pathsum(T, n, r, c):
    if cache[r][c] > -1:
        return cache[r][c]

    if r < n - 1:
        v = T[r][c] + max(pathsum(T, n, r + 1, c), pathsum(T, n, r + 1, c + 1))
    else:
        v = T[r][c]

    cache[r][c] = v
    return v


def path(T, n, r, c):
    P = []

    def inner(r, c):
        P.append(T[r][c])

        if r >= n - 1:
            return

        if cache[r + 1][c] > cache[r + 1][c + 1]:
            inner(r + 1, c)
        else:
            inner(r + 1, c + 1)

    inner(r, c)

    return P


for _ in range(C):
    N = int(input())

    T = [list(map(int, input().split())) for _ in range(N)]

    cache = [[-1] * n for n in range(1, N + 1)]

    v = pathsum(T, N, 0, 0)

    P = path(T, N, 0, 0)

    print(v)
    print(*P)
