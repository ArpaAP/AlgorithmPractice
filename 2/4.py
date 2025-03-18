from math import log, floor

N = int(input())

print(8 ** (floor(log(N, 4)) + 1))