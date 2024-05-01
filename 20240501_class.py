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
        # This method ensures that the Node with the lowest frequency has higher priority in the priority queue.
        return self.frequency < other.frequency

def huffman_tree(string):
    # Count frequencies of each character in the string
    counter = Counter(string)

    # Create a priority queue (heap) of nodes
    heap = [Node(val=char, frequency=count) for char, count in counter.items()]
    heapq.heapify(heap)

    # Combine nodes until one remains (the root of the Huffman Tree)
    while len(heap) > 1:
        left = heapq.heappop(heap)  # Pop the node with the smallest frequency
        right = heapq.heappop(heap)  # Pop the next smallest frequency node

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
    root = huffman_tree(s2)
    print("Huffman Codes for characters in string:")
    print_codes(root)
