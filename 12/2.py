# AP 12.2 - TSP: Dynamic Programming


N, M = map(int, input().split())

INF = 999

W = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    W[u][v] = w


def count(A):
    cnt = 0

    while A > 0:
        if A & 1:
            cnt += 1
        A >>= 1

    return cnt


def is_in(i, A):
    return A & (1 << (i - 2)) != 0


def diff(A, j):
    return A & ~(1 << (j - 2))


def minimum(i, A, D):
    min_value = INF
    minj = -1
    for j in range(2, N + 1):
        if not is_in(j, A):
            continue

        value = W[i][j] + D[j][diff(A, j)]
        if min_value > value:
            min_value = value
            minj = j

    return min_value, minj


def travel():
    subset_size = 1 << (N - 1)  # 정점 1을 제외한 나머지 정점들의 부분집합
    D = [[INF] * subset_size for _ in range(N + 1)]
    P = [[-1] * subset_size for _ in range(N + 1)]

    # Base case: 정점 i에서 정점 1로 직접 가는 경우
    for i in range(2, N + 1):
        D[i][0] = W[i][1]

    # k개의 정점을 포함하는 부분집합에 대해 처리
    for k in range(1, N - 1):
        for A in range(subset_size):
            if count(A) != k:
                continue

            for i in range(2, N + 1):
                if is_in(i, A):
                    continue

                D[i][A], minj = minimum(i, A, D)
                P[i][A] = minj

    # 모든 정점을 방문한 후 정점 1로 돌아가는 경우
    A = subset_size - 1  # 모든 정점 포함
    D[1][A], minj = minimum(1, A, D)
    P[1][A] = minj

    return D, P


def tour(v, A, P, path):
    if A == 0:
        path.append(1)
        return
    k = P[v][A]
    if k > 0:
        path.append(k)
        tour(k, diff(A, k), P, path)


D, P = travel()

# 최단 투어 길이 출력
min_length = D[1][(1 << (N - 1)) - 1]
print(min_length)

# 최단 투어 경로 출력
path = [1]
tour(1, (1 << (N - 1)) - 1, P, path)
print(" ".join(map(str, path)))

# D 테이블의 무한이 아닌 값들 출력
for i in range(1, N + 1):
    for j in range(1 << (N - 1)):
        if D[i][j] < INF:
            print(i, j, D[i][j])
