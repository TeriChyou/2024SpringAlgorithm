## 先預習最小生成樹

#以前寫的prim's algorithm
from queue import PriorityQueue as priority_queue
from math import inf
class Node:
    def __init__(self,id,**kwargs):
        self.id = id
        self.fst = self.lst = None

    def __iter__(self):
        return NodeIterator(self)

    def __repr__(self):
        return "Node(%d)"%self.id

class NodeIterator:
    def __init__(self,Node):
        self.prst = Node.fst

    def __next__(self):
        if self.prst == None:
            raise StopIteration()
        ret = self.prst
        self.prst = self.prst.nxt
        return ret

class Edge:
    def __init__(self,fr,to,**kwargs):
        if fr.fst == None:
            fr.fst = self
        else:
            fr.lst.nxt = self
        fr.lst = self
        self.to = to
        self.nxt = None
        self.w = 1 if 'w' not in kwargs else kwargs['w']

    def __repr__(self):
        return "Edge({},{},w = {})",format(self.fr,self.to,self.w)

class Graph:
    def __init__(self,V):
        self.nodecnt = V
        self.nodes = [Node(i) for i in range(V)]
        self.edges = []

    def add(self,u,v,**kwargs):
        self.edges.append(Edge(self.nodes[u],self.nodes[v],**kwargs))

    def MST_prim(self,begin):
        '''
        prim algorithm on a graph(with heap),
        returns the weight sum of the tree
        or -1 if impossible
        '''
        q = priority_queue()
        vis = [False for _ in range(self.nodecnt)]
        q.put((0,begin))
        ret = 0
        while not q.empty():
            prst = q.get()
            if vis[prst[1]]:
                continue
            vis[prst[1]] = True
            ret += prst[0]
            for i in self.nodes[prst[1]]:
                if not vis[i.to.id]:
                    q.put((i.w,i.to.id))
        if all(vis):
            return ret
        else:
            return -1

# Create a graph with 5 nodes
graph = Graph(5)

# Add edges to the graph with optional weights
graph.add(0, 1, w=10)
graph.add(1, 2, w=3)
graph.add(2, 3, w=1)
graph.add(3, 4, w=8)
graph.add(0, 4, w=5)
graph.add(1, 3, w=7)

# Compute the minimum spanning tree starting from node 0
mst_weight = graph.MST_prim(0)

# Print the weight of the minimum spanning tree
print("Weight of the MST:", mst_weight)
