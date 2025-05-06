# 9-2
# Huffman Algorithm

import heapq


class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


N = int(input())
chars = input().split()
freqs = list(map(int, input().split()))

M = int(input())
encode_targets = [input() for _ in range(M)]

K = int(input())
decode_targets = [input() for _ in range(K)]


class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman(chars, freqs):
    heap = []

    for c, f in zip(chars, freqs):
        heapq.heappush(heap, Node(c, f))

    if len(heap) == 1:
        node = heapq.heappop(heap)
        root = Node(None, node.freq, node, None)
        heapq.heappush(heap, root)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = Node("+", a.freq + b.freq, a, b)
        heapq.heappush(heap, merged)

    return heap[0]


def traverse(root, prefix, codes):
    if not root:
        return

    if root.left is None and root.right is None:
        codes[root.char] = prefix or "0"
    else:
        traverse(root.left, prefix + "0", codes)
        traverse(root.right, prefix + "1", codes)


def preorder(root, res):
    if not root:
        return

    if root.left is None and root.right is None:
        res.append(f"{root.char}:{root.freq}")
    else:
        res.append(f"{root.char}:{root.freq}")
        preorder(root.left, res)
        preorder(root.right, res)


def inorder(root, res):
    if not root:
        return

    inorder(root.left, res)

    if root.left is None and root.right is None:
        res.append(f"{root.char}:{root.freq}")
    else:
        res.append(f"{root.char}:{root.freq}")

    inorder(root.right, res)


root = build_huffman(chars, freqs)

codes = {}
traverse(root, "", codes)

pre = []
preorder(root, pre)
inord = []
inorder(root, inord)

print(" ".join(pre))
print(" ".join(inord))

for s in encode_targets:
    out = "".join(codes[ch] for ch in s)
    print(out)

for code in decode_targets:
    node = root
    decoded = []

    for bit in code:
        node = node.left if bit == "0" else node.right
        if node.left is None and node.right is None:
            decoded.append(node.char)
            node = root

    print("".join(decoded))
