from itertools import combinations

def travel(n, W):
    # Using float('inf') to represent infinite distances where no direct path exists
    inf = float('inf')
    # Initialize D for all one-element subsets consisting of each node except the starting node (index 0)
    D = { (i, 1 << (i - 1)): W[0][i] for i in range(1, n) }
    P = { (i, 1 << (i - 1)): 0 for i in range(1, n) }
    
    # Processing all subsets of increasing size from 1 up to n-1
    for k in range(1, n):
        for subset in combinations(range(1, n), k):
            subset_mask = sum([1 << (i-1) for i in subset])
            for i in subset:
                min_cost = inf
                min_prev = None
                # Considering nodes not in the current subset
                for j in range(1, n):
                    if j in subset and i != j:
                        current_mask = subset_mask ^ (1 << (i-1))
                        if (j, current_mask) in D:
                            cost = W[i][j] + D[(j, current_mask)]
                            if cost < min_cost:
                                min_cost = cost
                                min_prev = j
                if min_prev is not None:
                    D[(i, subset_mask)] = min_cost
                    P[(i, subset_mask)] = min_prev

    # Final step to complete the cycle to the starting point
    full_mask = (1 << (n-1)) - 1
    min_cost = inf
    min_prev = None
    for j in range(1, n):
        current_mask = full_mask ^ (1 << (j-1))
        if (j, current_mask) in D:
            cost = W[0][j] + D[(j, current_mask)]
            if cost < min_cost:
                min_cost = cost
                min_prev = j
    if min_prev is not None:
        D[(0, full_mask)] = min_cost
        P[(0, full_mask)] = min_prev

    # Reconstruct the route from the stored path
    path = [0]
    last = 0
    subset_mask = full_mask
    while subset_mask:
        prev = P.get((last, subset_mask))
        if prev is None:
            break
        path.append(prev)
        subset_mask ^= 1 << (prev-1)
        last = prev

    return D.get((0, full_mask), inf), path if path[-1] == 0 else "No valid path found"

# Example setup
n = 4
I = float('inf')
W = [
    [0, 2, 9, I],
    [1, 0, 6, 4],
    [I, 7, 0, 8],
    [6, 3, I, 0]
]

min_length, route = travel(n, W)
print("Minimum path length:", min_length)
print("Route:", route)
