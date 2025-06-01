# AP 12.3 - TSP: Branch-and-Bound

import heapq


class Node:
    def __init__(self, level, path, bound):
        self.level = level
        self.path = path
        self.bound = bound

    def __lt__(self, other):
        if self.bound != other.bound:
            return self.bound < other.bound
        return self.level < other.level


N, M = map(int, input().split())

INF = 0xFFFF

W = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    W[u][v] = w


def length(path):
    l = 0
    for i in range(len(path) - 1):
        l += W[path[i]][path[i + 1]]
    return l


def bound(node):
    current_cost = 0
    if len(node.path) > 1:
        current_cost = length(node.path)

    remaining = set(range(1, N + 1)) - set(node.path)

    total_min_outgoing = 0

    last_vertex = node.path[-1]
    if remaining:
        min_from_last = INF
        for v in remaining:
            min_from_last = min(min_from_last, W[last_vertex][v])
        if min_from_last == INF:
            return INF
        total_min_outgoing += min_from_last
    else:
        total_min_outgoing += W[last_vertex][1]

    for v in remaining:
        min_outgoing = INF
        for u in remaining:
            if u != v:
                min_outgoing = min(min_outgoing, W[v][u])
        if v != 1:
            min_outgoing = min(min_outgoing, W[v][1])

        if min_outgoing == INF:
            return INF
        total_min_outgoing += min_outgoing

    return current_cost + total_min_outgoing


def print_node(v):
    print(v.level, "INF" if v.bound >= INF else v.bound, *v.path)


def travel2():
    queue = []
    minlength = INF
    minpath = []

    v = Node(0, [1], 0)
    v.bound = bound(v)

    print_node(v)
    heapq.heappush(queue, v)

    while queue:
        v = heapq.heappop(queue)

        if v.bound < minlength:
            for i in range(2, N + 1):
                if i in v.path:
                    continue

                u = Node(v.level + 1, v.path + [i], 0)
                u.bound = bound(u)

                if u.level == N - 1:
                    complete_path = u.path + [1]
                    path_length = length(complete_path)

                    if path_length < minlength:
                        minlength = path_length
                        minpath = complete_path[:]

                    final_node = Node(u.level, complete_path, path_length)
                    print_node(final_node)
                else:
                    if u.level == N - 2:
                        remaining = list(set(range(2, N + 1)) - set(u.path))
                        complete_path = u.path + remaining + [1]

                        final_node = Node(u.level, complete_path, u.bound)
                        print_node(final_node)

                        actual_length = length(complete_path)
                        if actual_length < minlength:
                            minlength = actual_length
                            minpath = complete_path[:]
                    else:
                        print_node(u)

                    if u.bound < minlength:
                        heapq.heappush(queue, u)

    return minlength, minpath


minlength, minpath = travel2()
print(minlength)
print(*minpath)
