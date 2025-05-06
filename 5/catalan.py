N = int(input())


C = [1] * (N + 1)

for n in range(2, N + 1):
    s = 0

    for i in range(n // 2):
        s += C[i] * C[n - 1 - i]
    s *= 2

    if n % 2 == 1:
        s += C[n // 2] ** 2

    C[n] = s

print(C[N])
