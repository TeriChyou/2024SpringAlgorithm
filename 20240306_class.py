"""
class List:
    def __init__(self, s):
        if s is None:
            self.s = []
        else:
            self.s = s

    def add(self, c):
        self.s.append(c)

    def remove(self, c):
        self.s.remove(c)
"""
## 循序搜尋法(Sequential Search)
def seqsearch(n:int, S, x, location):
    location = 1
    while location <= n and S[location] != x:
        location += 1
    
    if location > n:
        location = 0

    return location
## 陣列加總
def summation(n:int, num):
    i = 0
    result = 0
    for i in range(n):
        result += num[i]
    
    return result
## 交換排序法(Exchange Sort)
def exchangesort(n:int, S):
    i = 0
    j = 0
    for i in range(n):
        for j in range(i + 1, n):
            if S[j] > S[i]:
                temp = S[j]
                S[j] = S[i]
                S[i] = temp
    
    return S

## Matrix Multiplying
### Complexity n^3
def matrixMult(n:int, A, B, res):
    i = 0
    j = 0
    k = 0
    for i in range(n):
        for j in range(n):
            res[i][j] = 0
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]

    return res

## Binary Search
# Complexity log_2(n)
# S needs to be sorted at first.
def binSearch(n:int, S, x, location):
    low = 1
    high = n
    location = 0
    while low <= high and location == 0:
        mid = int((low+high)/2)
        if x == S[mid]:
            location = mid
        elif x < S[mid]:
            high = mid - 1
        else:
            high = mid + 1

    return location

## Fibonacci Sequence
# This is a recursive method
# f0 = 0, f1 = 1, fn = fn-1 + fn-2
def fib(n:int):
    if n<0:
        return -1
    elif n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
# This is an example of DP(dynamic programming)
def elevatedFib(n:int):
    f = [0] * (n + 1)
    if n>0:
        f[1]=1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
    
    return f[n]

## Merge Sort
# This is a usage of divide and conquer
def mergesort(n:int, S):
    if(n>1):
        h = int(n / 2)
        m = n - h
        u = S[h:]
        v = S[:m]
        mergesort(h, u)
        mergesort(m, v)

def merge(h:int, m:int, u, v, s):
    i = 0
    j = 0
    k = 0
    while i <= h and j <= m:
        if u[i] < v[j]:
            s[k] = u[i]
            i+=1
        else:
            s[k] = v[j]
            j+=1
        k+=1
    if i>h:
        return 123 # not done yet
    else:
        return 123
## Usage
print(binSearch(6, exchangesort(6, [1,2,4,6,8,9]), 4, 0))
print(fib(6))
print(elevatedFib(6))