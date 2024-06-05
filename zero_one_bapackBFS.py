from queue import Queue

class Node:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight

class Knapsack:
    def __init__(self, weights, profits, capacity):
        self.weights = weights
        self.profits = profits
        self.capacity = capacity
        self.best = 0
        self.n = len(weights)

    def bound(self, node):
        if node.weight >= self.capacity:
            return 0
        else:
            profit_bound = node.profit
            j = node.level + 1
            total_weight = node.weight
            while j < self.n and total_weight + self.weights[j] <= self.capacity:
                total_weight += self.weights[j]
                profit_bound += self.profits[j]
                j += 1
            if j < self.n:
                profit_bound += (self.capacity - total_weight) * self.profits[j] / self.weights[j]
            return profit_bound

    def knapsack(self):
        Q = Queue()
        v = Node(-1, 0, 0)
        Q.put(v)
        while not Q.empty():
            v = Q.get()
            if v.level == self.n - 1:
                continue
            u = Node(v.level + 1, v.profit + self.profits[v.level + 1], v.weight + self.weights[v.level + 1])
            if u.weight <= self.capacity and u.profit > self.best:
                self.best = u.profit
                print(f"更新最佳利潤為: {self.best}")
            bound_u = self.bound(u)
            print(f"節點->利潤 {u.profit}, 重量 {u.weight}, 等級 {u.level} bound val:{bound_u}")
            if bound_u > self.best:
                Q.put(u)
                print(f"加入節點至佇列，利潤 {u.profit}, 重量 {u.weight}, 等級 {u.level}")
            u = Node(v.level + 1, v.profit, v.weight)
            bound_u = self.bound(u)
            print(f"節點->利潤 {u.profit}, 重量 {u.weight}, 等級 {u.level} bound val: {bound_u}")
            if bound_u > self.best:
                Q.put(u)
                print(f"加入節點至佇列，利潤 {u.profit}, 重量 {u.weight}, 等級 {u.level}")

# Example usage:
weights = [2, 5, 10, 5]
profits = [40, 30, 50, 10]
capacity = 16
knapsack = Knapsack(weights, profits, capacity)
knapsack.knapsack()
print(f"最大獲利為: {knapsack.best}")