# AP 11.1 - Fractional Knapsack


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


def knapsack1(W):
    maxprofit = totweight = 0

    S = []

    for i in range(N):
        if totweight + items[i].weight <= W:
            p, w = items[i].profit, items[i].weight
            maxprofit += p
            totweight += w
            S.append((w, p))
        else:
            p, w = (W - totweight) * items[i].profit_per_unit, W - totweight
            maxprofit += p
            totweight += w
            if w > 0:
                S.append((w, p))
            break

    return maxprofit, totweight, S


M = int(input())

for m in range(M):
    W = int(input())
    mp, tw, S = knapsack1(W)
    print(mp)

    for s in S:
        print(*s)
