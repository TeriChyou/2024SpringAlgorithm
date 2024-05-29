## 2024 05 29
class SubsetSum:
    def __init__(self, weights, target):
        self.weights = weights
        self.target = target
        self.solution = [0] * len(weights)
        self.results = []

    def sum_of_subsets(self, i, weight, total):
        if weight == self.target:
            result = [self.weights[i] for i in range(i+1) if self.solution[i] == 1]
            self.results.append(result)
            print(f"=========\n已找到解: {result} !!\n=========")
        elif i+1 < len(self.weights):
            self.solution[i + 1] = 1
            print(f"嘗試包含重量 {self.weights[i+1]}: {self.solution}")
            self.sum_of_subsets(i + 1, weight + self.weights[i + 1], total - self.weights[i + 1])
            self.solution[i + 1] = 0
            print(f"回溯搜尋中, 排除重量 {self.weights[i+1]}: {self.solution}")
            self.sum_of_subsets(i + 1, weight, total - self.weights[i + 1])

    def get_results(self):
        self.sum_of_subsets(-1, 0, sum(self.weights))
        return self.results

# 課本範例:
weights1 = [3, 4, 5, 6]
W1 = 13

weights2 = [2, 10, 13, 17, 22, 42]
W2 = 52
subset_sum = SubsetSum(weights2, W2)
print(subset_sum.get_results())
