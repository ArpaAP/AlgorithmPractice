N = int(input())

S = list(map(int, input().split()))

count = 0


def partition(low, high, pivotpoint):
    global count

    pivotitem = S[low]
    j = low

    for i in range(low + 1, high + 1):
        if S[i] < pivotitem:
            j += 1
            S[i], S[j] = S[j], S[i]
            count += 1

    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    count += 1

    return pivotpoint


def quicksort(low, high):
    if low < high:
        pivotpoint = 0
        pivotpoint = partition(low, high, pivotpoint)
        quicksort(low, pivotpoint - 1)
        quicksort(pivotpoint + 1, high)


quicksort(0, N - 1)

print(*S)
print(count)
