# AP 12.1 - 0-1 Knapsack: Branch-and-Bound

import heapq


class Node:
    def __init__(self, level, weight, profit, bound_value=0):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound_value = bound_value

    def __lt__(self, other):
        if self.bound_value != other.bound_value:
            return self.bound_value > other.bound_value
        return self.level < other.level


N, W = map(int, input().split())
weights = list(map(int, input().split()))
profits = list(map(int, input().split()))

# 아이템들을 profit/weight 순으로 정렬
items = [(i, profits[i] / weights[i], weights[i], profits[i]) for i in range(N)]
items.sort(key=lambda x: x[1], reverse=True)

# 배열 재구성
sorted_weights = [0] + [item[2] for item in items]
sorted_profits = [0] + [item[3] for item in items]
original_to_sorted = {items[i][0]: i + 1 for i in range(N)}
sorted_to_original = {i + 1: items[i - 1][0] for i in range(1, N + 1)}


def bound(u: Node):
    if u.weight >= W:
        return 0

    result = u.profit
    j = u.level + 1
    totweight = u.weight
    while j <= N and totweight + sorted_weights[j] <= W:
        totweight += sorted_weights[j]
        result += sorted_profits[j]
        j += 1

    k = j
    if k <= N:
        result += (W - totweight) * (sorted_profits[k] / sorted_weights[k])

    return result


def kanpsack5():
    queue = []
    maxprofit = 0

    # 초기 노드 생성 및 출력
    initial_node = Node(0, 0, 0)
    initial_bound = bound(initial_node)
    initial_node.bound_value = initial_bound
    print(0, 0, 0, int(initial_bound))
    heapq.heappush(queue, initial_node)

    while queue:
        v = heapq.heappop(queue)

        # 현재 노드의 bound가 maxprofit보다 작거나 같으면 pruning
        if v.bound_value <= maxprofit:
            continue

        if v.level == N:
            continue

        u = Node(
            v.level + 1,
            v.weight + sorted_weights[v.level + 1],
            v.profit + sorted_profits[v.level + 1],
        )

        left_bound = bound(u)
        u.bound_value = left_bound
        print(u.level, u.weight, u.profit, int(left_bound))

        if u.weight <= W and u.profit > maxprofit:
            maxprofit = u.profit

        if left_bound > maxprofit and u.level < N:
            heapq.heappush(queue, u)

        u = Node(v.level + 1, v.weight, v.profit)

        right_bound = bound(u)
        u.bound_value = right_bound
        print(u.level, u.weight, u.profit, int(right_bound))

        if right_bound > maxprofit and u.level < N:
            heapq.heappush(queue, u)

    return maxprofit


mp = kanpsack5()
print(mp)
