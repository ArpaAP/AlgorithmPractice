# 9-1
# Deadline Scheduling

N = int(input())

deadlines = [0] + list(map(int, input().split()))
profits = [0] + list(map(int, input().split()))


def is_feasible(K):
    for i in range(1, len(K)):
        if i > deadlines[K[i]]:
            return False

    return True


def schedule():
    J = [0, 1]

    for i in range(2, N + 1):
        K = J.copy()

        j = 1
        while j < len(K) and deadlines[K[j]] <= deadlines[i]:
            j += 1

        K.insert(j, i)

        if is_feasible(K):
            J = K.copy()

    return J


J = schedule()

feasible_profits = [profits[i] for i in J]
total = sum(feasible_profits)

print(total)
print(*feasible_profits[1:])
