N = int(input())
S = input()


def merge(a, b, c, d):
    top = [x + y for x, y in zip(a, b)]
    bottom = [x + y for x, y in zip(c, d)]

    return top + bottom


# idx는 현재 읽을 위치를 표시.
def decode(s, n, idx=0):
    c = s[idx]
    idx += 1

    # w를 만난 경우
    if c == "w":
        return [[0] * n for _ in range(n)], idx

    # b를 만난 경우
    elif c == "b":
        return [[1] * n for _ in range(n)], idx

    # x를 만난 경우
    else:
        m = n // 2
        lt, idx = decode(s, m, idx)
        rt, idx = decode(s, m, idx)
        lb, idx = decode(s, m, idx)
        rb, idx = decode(s, m, idx)

        return merge(lt, rt, lb, rb), idx


print(N)
matrix, _ = decode(S, N)

for row in matrix:
    print(*row)
