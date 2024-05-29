class MColoring:
    def __init__(self, graph, num_colors):
        self.graph = graph
        self.num_colors = num_colors
        self.coloring = [0] * len(graph)
        self.totalResultNum = 0
        self.totalResultArr = []

    def promising(self, i):
        for j in range(i):
            if self.graph[i][j] and self.coloring[i] == self.coloring[j]:
                return False
        return True

    def m_coloring(self, i):
        if self.promising(i):
            if i == len(self.graph) - 1:
                print(f"========\n找到結果:{self.coloring}\n========")
                self.totalResultNum += 1
                self.totalResultArr.append(list(self.coloring))
            else:
                for color in range(1, self.num_colors + 1):
                    self.coloring[i + 1] = color
                    print(f"嘗試顏色 {color} 號在節點 {i+2}: {self.coloring}")
                    self.m_coloring(i + 1)
                    print(f"回溯至顏色 {color} 號在節點 {i+2}")
                    self.coloring[i + 1] = 0

    def get_results(self):
        return self.totalResultNum, self.totalResultArr

# Example usage:
# p.245 5.5-18:                    
graph = [[0, 1, 0, 1, 0, 0],
         [1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1, 0],
         [0, 1, 0, 1, 0, 1],
         [0, 0, 1, 0, 1, 0]
         ]
m_coloring_problem = MColoring(graph, 3)
m_coloring_problem.m_coloring(-1)
print(m_coloring_problem.get_results())
