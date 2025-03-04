N = int(input())

S = list(map(int, input().split()))

count = 0

for i in range(N):
    for j in range(i + 1, N):
        if S[i] > S[j]:
            count += 1
            S[i], S[j] = S[j], S[i]

print(*S)
print(count)
