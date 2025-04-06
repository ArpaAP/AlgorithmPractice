N, M = map(int, input().split())

S = [0] + list(map(int, input().split()))
S.sort()

X = list(map(int, input().split()))

count = 0


def binsearch(x, low, high):
    global count
    count += 1

    if low > high:
        return 0

    mid = (low + high) // 2

    if x == S[mid]:
        return mid
    elif x < S[mid]:
        return binsearch(x, low, mid - 1)
    else:
        return binsearch(x, mid + 1, high)


for x in X:
    count = 0
    result = binsearch(x, 1, N)
    print(count, result)
