import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def encode(node, str, huffman_code):
    if node is None:
        return

    if node.left is None and node.right is None:
        huffman_code[node.char] = str

    encode(node.left, str + "0", huffman_code)
    encode(node.right, str + "1", huffman_code)

def buildHuffmanTree(str):
    if len(str) == 0:
        return

    pq = [Node(k, v) for k, v in str]
    heapq.heapify(pq)

    while len(pq) != 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)

        total = Node(None, left.freq + right.freq)
        total.left = left
        total.right = right

        heapq.heappush(pq, total)

    root = pq[0]

    huffmanCode = {}
    encode(root, "", huffmanCode)

    for k, v in huffmanCode.items():
        print(f"{k}: {v}")

str1 = [('A',12), ('B',7), ('I',18), ('M',10), ('S',9), ('X',5), ('Z',2)]
buildHuffmanTree(str1)