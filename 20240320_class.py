### Floyd Warshall Algorithm
## Firstly we have to get a n * n Adjacency Matrix(W) from the Graph
## Then we use the algorithm to get the D of the shortest path
## assuming W[i][j], i = j = n 
## We can gradually get D from D^(0~k), k = n, 1~k means adding vertexes into the path

# Floyd 1 O(n^3)
class FloydWarshall:
    def __init__(self, n, W):
        self.n = n
        self.D = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                self.D[i][j] = W[i][j]

    def minimum(self, a, b):
        return min(a, b)

    def floyd(self):
        for k in range(1, self.n + 1):
            for i in range(1, self.n + 1):
                for j in range(1, self.n + 1):
                    self.D[i][j] = self.minimum(self.D[i][j], self.D[i][k] + self.D[k][j])

    def print_result(self):
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                print(self.D[i][j], end=" ")
            print()

# Floyd2 O(n)
class FloydWarshallWithPath:
    def __init__(self, n, W):
        self.n = n
        self.D = [[0] * (n + 1) for _ in range(n + 1)]
        self.P = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                self.D[i][j] = W[i][j]

    def floyd_adv(self):
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                self.P[i][j] = 0

        for k in range(1, self.n + 1):
            print(f"第{k - 1}次")
            self.print_result()
            print("\0")
            for i in range(1, self.n + 1):
                for j in range(1, self.n + 1):
                    # 當比較的值出現變化後，紀錄該次的點K
                    if self.D[i][k] + self.D[k][j] < self.D[i][j]: 
                        self.P[i][j] = k
                        self.D[i][j] = self.D[i][k] + self.D[k][j]

    def path(self, q, r):
        if self.P[q][r] != 0:
            self.path(q, self.P[q][r])
            print("v" + str(self.P[q][r]), end=" ")
            self.path(self.P[q][r], r)

    def print_result(self):
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                print(self.D[i][j], end=" ")
            print()

    def print_P_result(self):
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                print(self.P[i][j], end=" ")
            print()
    def add_extra_row_and_column(matrix): # 如果輸入的矩陣沒有多一row和col
        n = len(matrix)
        # Create a new matrix with extra row and column
        new_matrix = [[0] * (n + 1) for _ in range(n + 1)]

        # Copy values from the original matrix to the new matrix
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                new_matrix[i][j] = matrix[i - 1][j - 1]

        return new_matrix


# Example usage:
n = 5
W = [[0, 0, 0, 0, 0, 0],
     [0, 0, 1, float('inf'), 1, 5],
     [0, 9, 0, 3, 2, float('inf')],
     [0, float('inf'), float('inf'), 0, 4, float('inf')],
     [0, float('inf'), float('inf'), 2, 0, 3],
     [0, 3, float('inf'), float('inf'), float('inf'), 0]]
# Floyd1
#floyd_algo = FloydWarshall(n, W)
#floyd_algo.floyd()
#floyd_algo.print_result()
#print("\0")
# FLoyd2
floyd_algo = FloydWarshallWithPath(n, W)
floyd_algo.floyd_adv()
floyd_algo.print_result()
print("\0")
floyd_algo.print_P_result()
# Example path reconstruction
q, r = 1, 3
print(f"Path from {q} to {r}:")
floyd_algo.path(q, r)
