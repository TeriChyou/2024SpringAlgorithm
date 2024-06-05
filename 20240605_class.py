# Best Fit TSP
import heapq

class Node:
    def __init__(self, level, path, bound, matrix):
        self.level = level
        self.path = path
        self.bound = bound
        self.matrix = matrix

def TSP(matrix):
    n = len(matrix)
    root = Node(0, [0], float('inf'), matrix)
    root.bound = bound(root, n)
    Q = []
    heapq.heappush(Q, (root.bound, id(root), root))
    best = float('inf')

    while Q:
        _, _, node = heapq.heappop(Q)
        print(f"處理節點: {node.path} with bound: {node.bound}")
        if node.bound < best:
            for i in range(n):
                if i not in node.path:
                    child = Node(node.level + 1, node.path + [i], float('inf'), matrix)
                    if child.level == n - 1:
                        child.path.append(0)
                        if total_cost(child) < best:
                            best = total_cost(child)
                            print(f"更新最佳路徑: {child.path} with cost: {best}")
                    else:
                        child.bound = bound(child, n)
                        if child.bound < best:
                            heapq.heappush(Q, (child.bound, id(child), child))
    return best

def total_cost(node):
    cost = 0
    for i in range(len(node.path) - 1):
        cost += node.matrix[node.path[i]][node.path[i+1]]
    return cost

def bound(node, n):
    bound = sum(node.matrix[node.path[-1]][i] for i in range(n) if i not in node.path)
    unvisited = [i for i in range(n) if i not in node.path]
    if len(unvisited) > 1:
        bound += min(node.matrix[i][j] for i in unvisited for j in unvisited if i != j)
    return bound

matrix = [
    [0, 14, 4, 10, 20],
    [14, 0, 7, 8, 7],
    [4, 5, 0, 7, 16],
    [11, 7, 9, 0, 2],
    [18, 7, 17, 4, 0]
]

print(f"最短路徑的總距離為: {TSP(matrix)}")