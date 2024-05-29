class Hamiltonian:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.vindex = [-1] * self.n
        self.vindex[0] = 0

    def promising(self, i):
        if i == self.n - 1 and not self.graph[self.vindex[self.n - 1]][self.vindex[0]]:
            return False
        if i > 0 and not self.graph[self.vindex[i - 1]][self.vindex[i]]:
            return False
        for j in range(1, i):
            if self.vindex[i] == self.vindex[j]:
                return False
        return True

    def hamiltonian(self, i):
        if self.promising(i):
            if i == self.n - 1:
                print(f"========\n找到結果: {[v + 1 for v in self.vindex]}\n========")  # Adding 1 to match the original 1-indexed algorithm
            else:
                for j in range(1, self.n):
                    self.vindex[i + 1] = j
                    print(f"嘗試頂點 v{j + 1} 在位置 v{i + 2}: {self.vindex}")  # Adding 1 to match the original 1-indexed algorithm
                    self.hamiltonian(i + 1)
                    print(f"回溯至 v{j + 1} 在位置 v{i + 2}")
                    self.vindex[i + 1] = -1

# Example usage:
graph = [[0, 1, 0, 0, 0, 0, 1, 1],
         [1, 0, 1, 0, 0, 0, 1, 1],
         [0, 1, 0, 1, 0, 1, 0, 0],
         [0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 1, 0, 1, 0, 1, 0],
         [1, 1, 0, 0, 0, 1, 0, 1],
         [1, 1, 0, 0, 0, 0, 1, 0]
         ]
hamiltonian = Hamiltonian(graph)
hamiltonian.hamiltonian(0)