class GeneSequenceAligner:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.m = len(x)
        self.n = len(y)
        self.memo = {}

    def opt(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        if i == self.m:
            result = 2 * (self.n - j)  # Cost of aligning remaining y with gaps
        elif j == self.n:
            result = 2 * (self.m - i)  # Cost of aligning remaining x with gaps
        else:
            if self.x[i] == self.y[j]:
                penalty = 0
            else:
                penalty = 1
            result = min(self.opt(i + 1, j + 1) + penalty,
                         self.opt(i + 1, j) + 2,
                         self.opt(i, j + 1) + 2)

        self.memo[(i, j)] = result
        return result

    def alignment_cost(self):
        return self.opt(0, 0)

    def trace_back(self):
        i, j = 0, 0
        aligned_x = []
        aligned_y = []
        while i < self.m or j < self.n:
            if i < self.m and j < self.n and (i + 1, j + 1) in self.memo and self.memo[(i, j)] == self.memo[(i + 1, j + 1)] + (0 if self.x[i] == self.y[j] else 1):
                aligned_x.append(self.x[i])
                aligned_y.append(self.y[j])
                i += 1
                j += 1
            elif i < self.m and (i + 1, j) in self.memo and self.memo[(i, j)] == self.memo[(i + 1, j)] + 2:
                aligned_x.append(self.x[i])
                aligned_y.append('-')
                i += 1
            elif j < self.n and (i, j + 1) in self.memo and self.memo[(i, j)] == self.memo[(i, j + 1)] + 2:
                aligned_x.append('-')
                aligned_y.append(self.y[j])
                j += 1

        return ''.join(aligned_x), ''.join(aligned_y)

    def print_matrix(self):
        # Print matrix
        matrix = [['-' for _ in range(self.n + 1)] for __ in range(self.m + 1)]
        for (i, j), cost in self.memo.items():
            matrix[i][j] = cost

        # Print header
        header = '    ' + '   '.join([c for c in self.y + '-'])
        print(header)

        # Print rows with headers
        for i in range(self.m + 1):
            row_label = self.x[i] if i < self.m else '-'
            row = f'{row_label} ' + ' '.join(f'{matrix[i][j]:>3}' for j in range(self.n + 1))
            print(row)

# Example usage
if __name__ == "__main__":
    SEQ1 = ["AACAGTTACC", "TAAGGTCA"]
    SEQ2 = ["CCGGGTTACCA", "GGAGTTCA"] 
    selected = SEQ2
    aligner = GeneSequenceAligner(selected[0], selected[1])
    print("Alignment Cost:", aligner.alignment_cost())
    aligned_seq1, aligned_seq2 = aligner.trace_back()
    print("Optimal Alignment Sequences:")
    print("X:", aligned_seq1)
    print("Y:", aligned_seq2)
    print("Memoized Results (R):")
    aligner.print_matrix()
