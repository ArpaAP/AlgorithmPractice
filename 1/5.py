# binsect 모듈 안쓰고 직접 구현한 버전으로 다시 제출합니다

N, M = map(int, input().split())

S = list(map(int, input().split()))
S.sort()

X = list(map(int, input().split()))

def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1

for x in X:
    idx = binary_search(S, x)
    if idx < N and S[idx] == x:
        print(f'{x} is in {idx + 1}.')
    else:
        print(f'{x} is not in S.')