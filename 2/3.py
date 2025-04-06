from math import log2, floor

N = int(input())

print(4 ** (floor(log2(N)) + 1))
