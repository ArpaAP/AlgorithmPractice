import sys
sys.setrecursionlimit(10**7)

count = 0

def next_power_of_2(n: int) -> int:
    """ n 이상의 가장 작은 2의 거듭제곱을 반환 """
    m = 1
    while m < n:
        m <<= 1
    return m

def madd(A, B):
    """ 같은 크기의 행렬 A, B에 대해 A + B """
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def msub(A, B):
    """ 같은 크기의 행렬 A, B에 대해 A - B """
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def mmult(A, B):
    """ 기본적인 행렬 곱셈 O(n^3) """
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C

def partition(M):
    """ 행렬 M을 4등분하여 반환.
        M의 크기는 항상 2의 거듭제곱이라고 가정함. """
    n = len(M)
    mid = n // 2
    A11 = [[M[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[M[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[M[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[M[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return A11, A12, A21, A22

def combine(A11, A12, A21, A22):
    """ 4등분된 행렬을 하나로 합침 """
    n2 = len(A11)  # 사분 행렬 한 변의 크기
    n = 2 * n2
    M = [[0]*n for _ in range(n)]
    for i in range(n2):
        for j in range(n2):
            M[i][j] = A11[i][j]
            M[i][j+n2] = A12[i][j]
            M[i+n2][j] = A21[i][j]
            M[i+n2][j+n2] = A22[i][j]
    return M

def strassen(A, B, threshold):
    global count
    count += 1

    n = len(A)

    if n <= threshold:
        return mmult(A, B)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = partition(A)
    B11, B12, B21, B22 = partition(B)

    M1 = strassen(madd(A11, A22), madd(B11, B22), threshold)
    M2 = strassen(madd(A21, A22), B11, threshold)
    M3 = strassen(A11, msub(B12, B22), threshold)
    M4 = strassen(A22, msub(B21, B11), threshold)
    M5 = strassen(madd(A11, A12), B22, threshold)
    M6 = strassen(msub(A21, A11), madd(B11, B12), threshold)
    M7 = strassen(msub(A12, A22), madd(B21, B22), threshold)

    C11 = msub(madd(madd(M1, M4), M7), M5)
    C12 = madd(M3, M5)
    C21 = madd(M2, M4)
    C22 = msub(madd(madd(M1, M3), M6), M2)

    C = combine(C11, C12, C21, C22)
    return C

N, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

M = next_power_of_2(N)

A_pad = [[0]*M for _ in range(M)]
B_pad = [[0]*M for _ in range(M)]

for i in range(N):
    for j in range(N):
        A_pad[i][j] = A[i][j]
        B_pad[i][j] = B[i][j]

C_pad = strassen(A_pad, B_pad, k)

C = [row[:N] for row in C_pad[:N]]

print(count)

for i in range(N):
    print(' '.join(map(str, C[i])))

