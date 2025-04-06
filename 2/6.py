N, M = map(int, input().split())


def count_collatz(n):
    count = 1

    while n != 1:
        count += 1

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    return count


def collatz(n):
    result = []

    while n != 1:
        result.append(n)

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    result.append(1)

    return result


pairs = [(x, count_collatz(x)) for x in range(N, M + 1)]

mx = max(pairs, key=lambda x: x[1])

print(mx[0], mx[1] - 1)
print(*collatz(mx[0]))
