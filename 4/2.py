threshold = int(input())
A = list(map(int, input()))[::-1]
B = list(map(int, input()))[::-1]

count = 0

def roundup_carry(v: list):
    carry = 0

    for i in range(len(v)):
        v[i] += carry
        carry = v[i] // 10
        v[i] %= 10

    if carry > 0:
        v.append(carry)

def ladd(a: list, b: list) -> list:
    c = [0] * max(len(a), len(b))

    for i in range(len(c)):
        if i < len(a):
            c[i] += a[i]
        if i < len(b):
            c[i] += b[i]

    roundup_carry(c)

    return c

def lmult(a: list, b: list) -> list:
    c = [0] * (len(a) + len(b) - 1)

    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]

    roundup_carry(c)

    return c

def pow_by_exp(u: list, m: int) -> list:
    if len(u) == 0:
        return []
    
    return [0] * m + u

def div_by_exp(u: list, m: int) -> list:
    if len(u) == 0:
        return []
    
    return u[m:]

def remove_leading_zeros(lst: list) -> list:
    while len(lst) > 0 and lst[-1] == 0:
        lst.pop()

    return lst

def rem_by_exp(u: list, m: int) -> list:
    if len(u) == 0:
        return []
    
    return remove_leading_zeros(u[:m])

def prod(u: list, v: list) -> list:
    global count
    count += 1

    n = max(len(u), len(v))

    if len(u) == 0 or len(v) == 0:
        return []

    if n <= threshold:
        return lmult(u, v)
    
    m = n // 2

    x = div_by_exp(u, m)
    y = rem_by_exp(u, m)
    w = div_by_exp(v, m)
    z = rem_by_exp(v, m)
    t1 = prod(x, w)
    t2 = pow_by_exp(t1, 2 * m)
    t3 = prod(x, z)
    t4 = prod(w, y)
    t5 = ladd(t3, t4)
    t6 = pow_by_exp(t5, m)
    t7 = prod(y, z)
    t8 = ladd(t2, t6)

    return ladd(t8, t7)

result = prod(A, B)

print(count)
print(*result[::-1], sep='')