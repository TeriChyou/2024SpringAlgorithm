# Huffman Tree
# source code from leetcode, and enhanced the code out put
from collections import Counter
import heapq

class Node:
    def __init__(self, val=None, frequency=0, left=None, right=None):
        self.val = val
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        # 這個方法確保擁有最低頻率的節點有最高的優先權
        return self.frequency < other.frequency

def huffman_tree(string):
    # 用counter去列出每個字母的數量
    counter = Counter(string)

    # 建立一個節點的優先權佇列
    heap = [Node(val=char, frequency=count) for char, count in counter.items()]
    heapq.heapify(heap)

    # 合併節點直至剩下一個(霍夫曼樹的根)
    while len(heap) > 1:
        left = heapq.heappop(heap)  # 削掉最低頻率的節點
        right = heapq.heappop(heap)  # 削掉下一個最低頻率的節點

        # Merge the two smallest nodes under a new combined node and push it back to the heap
        merged = Node(frequency=left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(heap, merged)

    # The remaining node is the root of the Huffman tree
    return heap[0]

def print_codes(node, prefix=""):
    # Base case: If the node is a leaf, print its character and the code (path from root)
    if node.val is not None:
        print(f"{node.val}: {prefix}")
    # Recursive case: Traverse left and right with updated prefix
    if node.left is not None:
        print_codes(node.left, prefix + "0")
    if node.right is not None:
        print_codes(node.right, prefix + "1")

# Example usage
if __name__ == "__main__":
    s = "engineer"
    s2 = "AAAAAAAAAAAAAAAAAAAAAAABBBBBCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDEEFFFFFFFFFFFGGGGGGGGGGGGGGGGGGGGHHHHH"
    s3 = "FFFFFFFFFFGGGGGGGGGGGGGGGGGGGGHHHHHAAAAAAAAAAAAAAAAAAAAAAABBBBBCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDEEF" # same as s2
    root = huffman_tree(s3)
    print("Huffman Codes for characters in string:")
    print_codes(root)
