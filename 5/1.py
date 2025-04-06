# 5-1
# Binomial Coefficient: Tabulation
# Timeout!

N, K = map(int, input().split())
K = min(K, N - K)

B = [0] * (K + 1)

for n in range(N + 1):
    prev = 1

    for k in range(min(n, K) + 1):
        if k == 0:
            B[k] = 1
        else:
            tmp = B[k]  # B[k]가 갱신되기 전 값 저장.
            B[k] = (B[k] + prev) % 10007  # 계산
            prev = tmp  # 갱신되기 전 값을 prev로 설정.

print(B[K])
