# 6-2
# Optimal Binary Search Tree

import sys
from typing import Optional

N = int(input())
K = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def minimum(i, j, s, A):
    min_value = sys.maxsize
    min_k = 0
    w = s[j] - s[i - 1]

    for k in range(i, j + 1):
        left = A[i][k - 1] if k > i else 0
        right = A[k + 1][j] if k < j else 0
        value = left + right + w

        if min_value > value:
            min_value = value
            min_k = k

    return min_value, min_k


def optsearchtree(n, p, A, R):
    s = [0] * (n + 1)

    for i in range(1, n + 1):
        s[i] = s[i - 1] + p[i]

    for i in range(1, n + 1):
        A[i][i - 1] = 0
        A[i][i] = p[i]
        R[i][i - 1] = 0
        R[i][i] = i

    for diag in range(1, n):
        for i in range(1, n - diag + 1):
            j = i + diag
            A[i][j], k = minimum(i, j, s, A)
            R[i][j] = k

    return A[1][n]


def tree(i, j, K, R):
    k = R[i][j]
    if k == 0:
        return

    node = Node(K[k])
    node.left = tree(i, k - 1, K, R)
    node.right = tree(k + 1, j, K, R)

    return node


def print_diagonal(M):
    for i, row in enumerate(M[1:]):
        print(*row[i:])


def preorder(node: Optional[Node]):
    result = []

    def inner(node: Optional[Node]):
        if node is None:
            return
        result.append(node.data)
        inner(node.left)
        inner(node.right)

    inner(node)
    return result


def inorder(node: Optional[Node]):
    result = []

    def inner(node: Optional[Node]):
        if node is None:
            return
        inner(node.left)
        result.append(node.data)
        inner(node.right)

    inner(node)
    return result


A = [[0] * (N + 1) for _ in range(N + 2)]
R = [[0] * (N + 1) for _ in range(N + 2)]

optvalue = optsearchtree(N, p, A, R)
root = tree(1, N, K, R)

print_diagonal(A)
print_diagonal(R)
print(optvalue)
print(*preorder(root))
print(*inorder(root))
