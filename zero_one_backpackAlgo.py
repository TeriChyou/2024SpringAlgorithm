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
            return False
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
        v = Node(-1, 0, 0)
        self.check_node(v)

    def check_node(self, v):
        if v.profit > self.best and v.weight <= self.capacity:
            self.best = v.profit
        if v.level + 1 < self.n:
            u = Node(v.level + 1, v.profit + self.profits[v.level + 1], v.weight + self.weights[v.level + 1])
            bound_u = self.bound(u)
            print(f"節點的界限值，利潤 {u.profit}, 重量 {u.weight}, 等級 {u.level} 是 {bound_u}")
            if bound_u > self.best:
                print(f"前往階層:{u.level + 1} => 獲利:{u.profit} 重量:{u.weight}")
                self.check_node(u)
            else:
                print(f"回溯至階層:{u.level + 1} => 獲利:{u.profit} 重量:{u.weight}")
            u = Node(v.level + 1, v.profit, v.weight)
            bound_u = self.bound(u)
            print(f"節點的界限值，利潤 {u.profit}, 重量 {u.weight}, 等級 {u.level} 是 {bound_u}")
            if bound_u > self.best:
                print(f"前往階層:{u.level + 1} => 獲利:{u.profit} 重量:{u.weight}")
                self.check_node(u)
            else:
                print(f"回溯至階層:{u.level + 1} => 獲利:{u.profit} 重量:{u.weight}")

# Example usage:
weights = [2, 5, 10, 5]
profits = [40, 30, 50, 10]
capacity = 16
knapsack = Knapsack(weights, profits, capacity)
knapsack.knapsack()
print(f"最大獲利為: {knapsack.best}")
# false = 沒用了 回溯