class UnionFind:
    """Union-Find data structure with path compression and union by rank."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append(Edge(u, v, weight))

    def kruskal(self):
        """Kruskal's algorithm to find the MST of the graph."""
        # Sort edges by weight
        self.edges.sort()

        # Initialize Union-Find
        uf = UnionFind(self.V)

        mst_weight = 0
        mst_edges = []

        for edge in self.edges:
            if uf.find(edge.u) != uf.find(edge.v):
                uf.union(edge.u, edge.v)
                mst_weight += edge.weight
                mst_edges.append(edge)

        # Check if we have a valid MST (V-1 edges)
        if len(mst_edges) != self.V - 1:
            return -1  # No valid MST exists

        return mst_weight


# Example 1: Simple connected graph
graph = Graph(4)
graph.add_edge(0, 1, 1)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 2)
graph.add_edge(1, 3, 6)
graph.add_edge(2, 3, 3)

mst_weight = graph.kruskal()
print("MST Weight:", mst_weight)  # Output should be 6
