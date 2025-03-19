N = int(input())

S = list(map(int, input().split()))

count = 0

def merge(h, m, left, right, ls):
    global count

    count += 1

    i = 0
    j = 0
    k = 0

    while i < h and j < m:
        if left[i] < right[j]:
            ls[k] = left[i]
            i += 1
        else:
            ls[k] = right[j]
            j += 1
        k += 1

    while i < h:
        ls[k] = left[i]
        i += 1
        k += 1

    while j < m:
        ls[k] = right[j]
        j += 1
        k += 1


def mergesort(n, ls):
    if n == 1:
        return
    
    h = n // 2
    m = n - h

    left = ls[:h]
    right = ls[h:]

    mergesort(h, left)
    mergesort(m, right)

    merge(h, m, left, right, ls)

result = mergesort(N, S)

print(*S)
print(count)