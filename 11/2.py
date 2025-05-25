# AP 11.2 - 0-1 Knapsack: Dynamic Programming


class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.profit_per_unit = profit // weight


N = int(input())

weights = list(map(int, input().split()))
profits = list(map(int, input().split()))

items = [Item(w, p) for w, p in zip(weights, profits)]
items.sort(key=lambda item: item.profit_per_unit, reverse=True)

weights = [it.weight for it in items]
profits = [it.profit for it in items]


def knapsack3(N, W) -> int:
    if N == 0 or W <= 0:
        return 0

    key = (N, W)
    if key in P:
        return P[key]

    without_i = knapsack3(N - 1, W)

    if weights[N - 1] <= W:
        with_i = profits[N - 1] + knapsack3(N - 1, W - weights[N - 1])
        P[key] = max(without_i, with_i)
    else:
        P[key] = without_i

    return P[key]


M = int(input())

for m in range(M):
    W = int(input())
    P = {}
    mp = knapsack3(N, W)
    print(mp)

    for k, v in sorted(P.items()):
        print(*k, v)
