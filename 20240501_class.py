from itertools import combinations

def travel(n, W):
    inf = float('inf')
    # 用字典(dict)收錄各個節點(nodes)到達各個子集(subsets)的最小路徑長(min cost)
    D = {}
    P = {}

    # 初始化可能性:各個節點回到初始節點的路徑
    for i in range(1, n):
        D[(i, 1 << (i-1))] = W[i][0]
        P[(i, 1 << (i-1))] = 0

    # 對各個子集的大小作迭代
    for k in range(1, n):
        # 產生所有從1 ~ n-1的子集(排除起始點 因為起始點到起始點是0) 這裡的1是第二個點(python is 0-indexed)
        for subset in combinations(range(1, n), k):
            # 產生子集的位元遮罩(bit mask)
            subset_mask = sum([1 << (i-1) for i in subset])
            # 嘗試找出子集的結束點
            for i in subset:
                # 計算從子集中任何節點j到結束點i的最小路徑(cost)
                min_cost = inf
                min_prev = None
                for j in subset:
                    if j != i:
                        prev_mask = subset_mask & ~(1 << (i-1))
                        if (j, prev_mask) in D:
                            cost = W[i][j] + D[(j, prev_mask)]
                            if cost < min_cost:
                                min_cost = cost
                                min_prev = j
                if min_prev is not None:
                    D[(i, subset_mask)] = min_cost
                    P[(i, subset_mask)] = min_prev

    # 計算任何一子集，也就是初次二次...DP過後的子集，到初始節點的路徑長
    min_cost = inf
    min_prev = None
    full_mask = (1 << (n-1)) - 1
    for i in range(1, n):
        if (i, full_mask) in D:
            cost = W[0][i] + D[(i, full_mask)]
            if cost < min_cost:
                min_cost = cost
                min_prev = i
    if min_prev is not None:
        D[(0, full_mask)] = min_cost
        P[(0, full_mask)] = min_prev

    # 建立最短路徑
    if min_prev is None:
        return inf, ["No valid path found"]
    
    path = [0]
    last = min_prev
    subset_mask = full_mask
    while last != 0:
        path.append(last)
        next_mask = subset_mask & ~(1 << (last-1))
        last = P[(last, subset_mask)]
        subset_mask = next_mask

    path.append(0)  # 回到初始點
    path.reverse()
    return min_cost, path
# Example setup
n = 5
I = float('inf')
W = [
    [0, 2, 9, I],
    [1, 0, 6, 4],
    [I, 7, 0, 8],
    [6, 3, I, 0]
]
W2 = [
    [0, 8, 13, 18, 20],
    [3, 0, 7, 8, 10],
    [4, 11, 0, 10, 7],
    [6, 6, 7, 0, 11],
    [10, 6, 2, 1, 0]
]
W3 = [
    [0, 14, 4, 10, 20],
    [14, 0, 7, 8, 7],
    [4, 5, 0, 7, 16],
    [11, 7, 9, 0, 2],
    [18, 7, 17, 4, 0]
]
chosen = W3
min_length, route = travel(len(chosen[0]), chosen)
print("Minimum path length:", min_length)
print("Route:", [i+1 for i in route]) # i+1 just while python is zero indexed
