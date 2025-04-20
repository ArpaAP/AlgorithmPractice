# 7-4
# Activity Selection: Meeting Room Reservation

N = int(input())

pairs = [tuple(map(int, input().split())) for _ in range(N)]

endtime = pairs[0][1]

S = [pairs[0]]

for s, e in pairs[1:]:
    if s >= endtime:
        endtime = e
        S.append((s, e))

print(len(S))

for s in S:
    print(*s)
