N = int(input())

F = [0, 1]

for i in range(N):
    F.append((F[-1] + F[-2]) % 1000000)

print(F[N])
