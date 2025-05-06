# 9-3
# Fibonacci Decomposition

N = int(input())

F = [0, 1]

i = 2

while F[-1] < N:
    F.append(F[i - 1] + F[i - 2])

    i += 1

result = []

while N > 0:
    f = F[-1]
    while f > N:
        f = F.pop()

    result.append(f)
    N -= f

result.reverse()

for r in result:
    print(r)
