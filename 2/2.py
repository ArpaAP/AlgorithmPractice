from math import log2, floor, ceil

N, M, P = map(int, input().split())

first = ceil((2 * N) / 4)
second = floor(log2(2 * M)) + 1
third = floor(log2(4 * P)) + 1

print(first * second * third)