## QUICK SORT
class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def qsMain(self):
        self.quicksort(0, len(self.arr) - 1)
        print("Sorted array is:", self.arr)

    def quicksort(self, low, high):
        if low < high:
            pivotpoint = self.partition(low, high)
            print(self.arr)  # Print the array after partitioning
            self.quicksort(low, pivotpoint - 1)
            self.quicksort(pivotpoint + 1, high)

    def partition(self, low, high):
        pivotitem = self.arr[low]
        j = low
        for i in range(low + 1, high + 1):
            if self.arr[i] < pivotitem:
                j += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        pivotpoint = j
        self.arr[low], self.arr[pivotpoint] = self.arr[pivotpoint], self.arr[low]
        return pivotpoint

# Example usage
arr = [15, 22, 13, 27, 12, 10, 20, 25]
# midterm
midterm = [123, 34, 189, 56, 150, 12, 9, 240]
qs = QuickSort(midterm)
qs.qsMain()

## Large Int Product
class LargeIntegerMultiplication:
    def __init__(self, threshold=10):
        self.threshold = threshold

    def multiply(self, u, v):
        # Public method to initiate multiplication
        result = self._prod(u, v)
        print("The product of", u, "and", v, "is:", result)
        return result

    def _prod(self, u, v):
        # Recursive method to calculate product
        n = max(len(str(u)), len(str(v)))
        
        if u == 0 or v == 0:
            return 0
        elif n <= self.threshold:  # Base case
            return u * v
        else:
            m = n // 2
            
            # Splitting the digit sequences
            x = u // 10**m
            y = u % 10**m
            w = v // 10**m
            z = v % 10**m
            
            # Recursive multiplication
            p1 = self._prod(x, w)
            p2 = self._prod(x, z)
            p3 = self._prod(y, w)
            p4 = self._prod(y, z)
            
            # Combine the products
            return p1 * 10**(2*m) + (p2 + p3) * 10**m + p4

# Example usage
u = 12345678901234567890
v = 98765432109876543210
lim = LargeIntegerMultiplication()
result = lim.multiply(u, v)

## Binomial Coefficient

# Divide and Conquer
def bin(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return bin(n-1, k-1) + bin(n-1, k)

# Example usage
n, k = 5, 2
print(f"C({n}, {k}) =", bin(n, k))


# DP

def binCoeff(n, k):
    B = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]
    print(B)
    return B[n][k]

# Example usage
n, k = 6, 6
print(f"C({n}, {k}) =", binCoeff(n, k))


