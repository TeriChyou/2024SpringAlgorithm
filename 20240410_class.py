import numpy as np
from fractions import Fraction
# req pip install numpy
# node class
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
# Normal Search Tree
def search(tree, keyin):
    p = tree
    while p:
        if p.key == keyin:
            return p
        elif keyin < p.key:
            p = p.left
        else:
            p = p.right
    return None
# ConstrucOBST
def constructOBST(i, j, R, keys):
    if i <= j:
        k = R[i][j]
        if isinstance(k, list):  # 將第一個可能性抓出來用
            k = k[0]
        node = TreeNode(keys[k-1])  # K保證是int
        node.left = constructOBST(i, k-1, R, keys)
        node.right = constructOBST(k+1, j, R, keys)
        return node
    else:
        return None
# OBST with visualization
def optSearchWithVisualization(n, p):
    A = np.zeros((n+2, n+1))
    R = [[[] for _ in range(n+1)] for _ in range(n+2)]  # 用list儲存可能的根
    
    for i in range(1, n+1):
        A[i][i-1] = 0
        A[i][i] = p[i-1]  # 更改係數(因為py是0-indexed)
        R[i][i] = [i]  # 把可能的根存進list
    
    # Visualize initial state
    print("初始矩陣A A:")
    printMatrixAAsFractions(A)
    
    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            min_val = float('inf')
            min_roots = []  # 將最小的可能性儲存的list
            for k in range(i, j+1):
                q = A[i][k-1] + A[k+1][j] + sum(p[i-1:j])  # 0-indexed 所以要調整
                if q < min_val:
                    min_val = q
                    min_roots = [k]  # 最小值找到了，根的列表重製
                elif q == min_val:
                    min_roots.append(k)  # 若最小值有重複則都列進list
            A[i][j] = min_val
            R[i][j] = min_roots 
            
            # 分析
            print(f"更新後的矩陣A, 設A[{i}][{j}] = {Fraction(min_val).limit_denominator(1000)}, 可能的樹根: {R[i][j]}")
            printMatrixAAsFractions(A)
    
    minavg = A[1][n]
    return A, minavg, R
def visualizeTreeNode(node, level=0):
    if node is not None:
        visualizeTreeNode(node.right, level + 1)
        print('    ' * level + f'-> {node.key}')
        visualizeTreeNode(node.left, level + 1)

# print funcs
def printMatrixR(R):
    print("矩陣 R:")
    rows = len(R)
    for i in range(1, rows-1):  # 更改長度避免印出不必要的列
        cols = len(R[i])
        for j in range(1, cols):
            roots = R[i][j]
            if isinstance(roots, list):  # 檢查是否有兩種以上可能性
                print(f"{roots}", end="\t")
            else:  # 沒有兩種可能性的話
                print(f"{roots}", end="\t")
        print()  # \n
def printMatrixA(A):
    print("Matrix A:")
    rows, cols = A.shape
    for i in range(1, rows-1):  # 更改長度避免印出不必要的列
        for j in range(cols):
            print(f"{A[i][j]:.2f}", end="\t")
        print()  # \n
def printMatrixAAsFractions(A):
    print("Matrix A (as fractions):")
    rows, cols = A.shape
    for i in range(1, rows-1): 
        for j in range(cols):
            # 轉成分數 和 上限值
            fraction = Fraction(A[i][j]).limit_denominator(1000)
            print(f"{fraction}", end="\t")
        print()  # \n

def main(keys, p):
    n = len(keys)
    A, minavg, R = optSearchWithVisualization(n, p)
    obst_root = constructOBST(1, n, R, keys)
    # printMatrixA(A)
    printMatrixR(R)
    visualizeTreeNode(obst_root)
    print(minavg)
# 課本P.129 範例3.9
k1 = [1, 2, 3, 4]
p1 = [3/8, 3/8, 1/8, 1/8]
# 課本P.148 22題
k2 = [1, 2, 3, 4, 5, 6] # CASE, ELSE, END, IF, OF, THEN
p2 = [0.05, 0.15, 0.05, 0.35, 0.05, 0.35]
# Midterm
k3 = ['k1', 'k2', 'k3', 'k4', 'k5']
p3 = [0.25, 0.2, 0.05, 0.2, 0.3]

main(k3, p3)
