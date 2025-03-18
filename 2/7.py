N, K = map(int, input().split())

count = 0
ls = []

def hanoi(n, src, via, dst):
    global count

    count += 1

    if n == 1:
        ls.append((src, dst))
    else:
        hanoi(n - 1, src, dst, via)
        hanoi(1, src, via, dst)
        hanoi(n - 1, via, src, dst)

hanoi(N, 'A', 'B', 'C')
print(f'{ls[K - 1][0]} -> {ls[K - 1][1]}')
print(count)