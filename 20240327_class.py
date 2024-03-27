## Min Multi
class MatrixChain:
    def __init__(self, d):
        self.d = d  # dimensions of matrices
        self.n = len(d) - 1  # number of matrices
        self.M = [[0 for _ in range(self.n + 1)] for _ in range(self.n + 1)]
        self.P = [[0 for _ in range(self.n + 1)] for _ in range(self.n + 1)]

    def minMult(self):
        for i in range(1, self.n + 1):
            self.M[i][i] = 0
        for diagonal in range(1, self.n):
            for i in range(1, self.n - diagonal + 1):
                # 斜線座標值
                j = i + diagonal
                # 窮舉
                min_val = float('inf')
                for k in range(i, j):
                    q = self.M[i][k] + self.M[k + 1][j] + self.d[i - 1] * self.d[k] * self.d[j]
                    # 印出目前的詳細計算
                    print(f"計算 M[{i}][{j}] 減掉 在k={k}處分開計算: Cost = {q}")
                    if q < min_val:
                        min_val = q
                        self.P[i][j] = k
                        # 當新的最小值找到就印
                        print(f"新的最小值 M[{i}][{j}] 在 k={k}找到: 乘法次數 = {min_val}")
                self.M[i][j] = min_val
                # 印出最終的結果
                print(f" 從矩陣 A{i} 到 A{j}的乘法次數最小值: {min_val},  在k={self.P[i][j]}分開")
                print("---")
        return self.M[1][self.n]


    def order(self, i, j):
        if i == j:
            print(f"A{i}", end='')
        else:
            print("(", end='')
            k = self.P[i][j]
            self.order(i, k)
            self.order(k + 1, j)
            print(")", end='')

    def printM(self):
        print("M matrix:")
        for row in range(1, self.n + 1):
            for col in range(1, self.n + 1):
                # :>7 is for the align ment
                print(f"{self.M[row][col]:>7}", end=" ")
            print()

# Example usage
if __name__ == "__main__":
    # Example matrix dimensions
    # For matrices A1, A2, A3with dimensions 10x100, 100x5, 5x50 respectively
    d = [10, 100, 5, 50]
    # 課堂範例A1(5x2), A2(2x3),A3(3x4), A4(4x6), A5(6x7), A6(7x8)
    d2 = [5, 2, 3, 4, 6, 7, 8]
    mc = MatrixChain(d2)
    min_cost = mc.minMult()
    print("Minimum number of multiplications is:", min_cost)
    print("Optimal multiplication order: ", end='')
    mc.order(1, len(d2)-1)
    mc.printM()
