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

        # 將兩個最小的節點合併到一個新的組合節點下並將其推回heap中
        merged = Node(frequency=left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(heap, merged)

    # 最後一個節點就是霍夫曼樹的根啦
    return heap[0]

def print_codes(node, prefix=""):
    # 印出結果: 若節點為樹葉, 印出字母及編碼 (從根的路徑編碼)
    if node.val is not None:
        print(f"{node.val}: {prefix}")
    # 遞迴: 追蹤左右子樹去更新前綴
    if node.left is not None:
        print_codes(node.left, prefix + "0")
    if node.right is not None:
        print_codes(node.right, prefix + "1")

# Example usage
if __name__ == "__main__":
    s = "engineer"
    s2 = "AAAAAAAAAAAAAAAAAAAAAAABBBBBCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDEEFFFFFFFFFFFGGGGGGGGGGGGGGGGGGGGHHHHH" 
    s3 = "FFFFFFFFFFGGGGGGGGGGGGGGGGGGGGHHHHHAAAAAAAAAAAAAAAAAAAAAAABBBBBCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDEEF" # same as s2
    s4 = "AAAAAAAAAAAABBBBBBBIIIIIIIIIIIIIIIIIIMMMMMMMMMMSSSSSSSSSXXXXXZZ"
    root = huffman_tree(s4)
    print("Huffman Codes for characters in string:")
    print_codes(root)

# Big(O)
# Frequency counting: O(n) -> n = length of string
# Heap Operation: O(klogk) -> k = unique characters in string
# Tree traversal code: O(k)