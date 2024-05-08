## divide and conquer method
## dp version in other filed called dpSeqAlign

class GeneSequenceAligner:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.m = len(x)
        self.n = len(y)
        self.memo = {}

    def opt(self, i, j):
        # Check if the result is already computed
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        if i == self.m:
            result = 2 * (self.n - j)
        elif j == self.n:
            result = 2 * (self.m - i)
        else:
            if self.x[i] == self.y[j]:
                penalty = 0
            else:
                penalty = 1
            result = min(self.opt(i + 1, j + 1) + penalty,   # No gap
                         self.opt(i + 1, j) + 2,             # Gap in y
                         self.opt(i, j + 1) + 2)             # Gap in x

        # Save the result in the memoization dictionary
        self.memo[(i, j)] = result
        return result

    def alignment_cost(self):
        return self.opt(0, 0)

# Example usage:
if __name__ == "__main__":
    seq1 = "AGTACG"
    seq2 = "ACATG"
    aligner = GeneSequenceAligner(seq1, seq2)
    print("Alignment Cost:", aligner.alignment_cost())
