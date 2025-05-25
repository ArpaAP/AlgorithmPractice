# AP 11.3 - 0-1 Knapsack: Backtracking


class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.profit_per_unit = profit // weight


N, W = map(int, input().split())

weights = list(map(int, input().split()))
profits = list(map(int, input().split()))

items = [Item(w, p) for w, p in zip(weights, profits)]
items.sort(key=lambda item: item.profit_per_unit, reverse=True)

weights = [0] + [it.weight for it in items]
profits = [0] + [it.profit for it in items]


def promising(i, p, w):
    global maxprofit

    if w > W:
        # 초과된 무게에 대한 이익 계산
        excess_weight = w - W
        # 현재 아이템(i)의 단위 이익 계산
        if i > 0:
            unit_profit = profits[i] / weights[i]
            # 초과된 무게에 해당하는 이익을 차감
            bound = p - excess_weight * unit_profit
        else:
            bound = p
        print(i, w, p, int(bound), maxprofit)
        return False

    j = i + 1
    bound = p
    totweight = w

    while j <= N and totweight + weights[j] <= W:
        totweight += weights[j]
        bound += profits[j]
        j += 1

    k = j

    if k <= N and totweight < W:
        unit_profit = profits[k] // weights[k]
        bound += (W - totweight) * unit_profit

    print(i, w, p, int(bound), maxprofit)

    return bound > maxprofit


def knapsack4(i, p, w):
    global maxprofit, bestset, include

    if w <= W and p > maxprofit:
        maxprofit = p
        bestset = include.copy()

    if promising(i, p, w):
        include[i + 1] = True
        knapsack4(i + 1, p + profits[i + 1], w + weights[i + 1])
        include[i + 1] = False
        knapsack4(i + 1, p, w)


maxprofit = 0
include = [False] * (N + 1)
bestset = []

knapsack4(0, 0, 0)

print(maxprofit)

for i in range(1, N + 1):
    if bestset[i]:
        print(weights[i], profits[i])
