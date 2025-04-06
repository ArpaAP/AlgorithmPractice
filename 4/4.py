N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def quadtree(matrix):
    n = len(matrix)

    if n == 1:
        return "b" if matrix[0][0] else "w"

    m = n // 2

    lt = quadtree([r[:m] for r in matrix[:m]])
    rt = quadtree([r[m:] for r in matrix[:m]])
    lb = quadtree([r[:m] for r in matrix[m:]])
    rb = quadtree([r[m:] for r in matrix[m:]])

    ls = [lt, rt, lb, rb]

    # 네 사분면 모두 같고 그게 x가 아니면
    if lt == rt == lb == rb and lt != "x":
        return lt

    return "x" + "".join(ls)


result = quadtree(matrix)

print(result)
