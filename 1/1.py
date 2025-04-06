# index 메서드 사용하지 않고 직접 구현하여 재제출합니다

N, M = map(int, input().split())

S = list(map(int, input().split()))

X = list(map(int, input().split()))


def index(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1


for x in X:
    idx = index(S, x)
    if idx > -1:
        print(f"{x} is in {idx + 1}.")
    else:
        print(f"{x} is not in S.")
