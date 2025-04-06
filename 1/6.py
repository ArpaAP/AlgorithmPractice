count = 0


def fibo(n):
    global count

    count += 1

    if n == 0:
        return 0

    if n == 1:
        return 1

    return (fibo(n - 1) + fibo(n - 2)) % 1000000


N = int(input())

print(fibo(N))
print(count)
