# 5-2
# Binomial Coefficient: Memoization

import sys

sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
K = min(K, N - K)

dp = {}
count = 0


def binom(n, k):
    global count

    count += 1

    if k == 0 or k == n:
        return 1

    if (n, k) in dp:
        return dp[(n, k)]

    r = (binom(n - 1, k - 1) + binom(n - 1, k)) % 10007
    dp[(n, k)] = r

    return r


print(binom(N, K))
print(count)
