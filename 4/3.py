N = int(input())

matrix = [[1, 1], [1, 0]]

def multiply(a, b):
    n = len(a)
    m = len(b[0])
    l = len(b)
    
    result = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(l):
                result[i][j] += a[i][k] * b[k][j]
                result[i][j] %= 10007
    
    return result

def power(matrix, k):
    if k == 1:
        return matrix
    elif k % 2 == 0:
        sub = power(matrix, k // 2)
        return multiply(sub, sub)
    else:
        sub = power(matrix, k // 2)
        return multiply(multiply(sub, sub), matrix)
    
p = power(matrix, N)

result = multiply(p, [[1], [0]])

print(result[1][0])