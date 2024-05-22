import heapq

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.distances = {vertex: float('infinity') for vertex in graph}
        self.paths = {vertex: [] for vertex in graph}

    def find_shortest_paths(self, start):
        # Priority queue to keep track of the vertices and their distances
        priority_queue = [(0, start)]

        # Set the distance to the starting vertex as 0
        self.distances[start] = 0

        while priority_queue:
            # Get the vertex with the smallest distance
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # If the current distance is greater than the known distance, skip
            if current_distance > self.distances[current_vertex]:
                continue

            # Explore neighboring vertices
            for neighbor, edge_weight in self.graph[current_vertex]:
                distance = current_distance + edge_weight

                # If a shorter path is found, update the distance and path
                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    self.paths[neighbor] = self.paths[current_vertex] + [current_vertex]
                    heapq.heappush(priority_queue, (distance, neighbor))

    def get_shortest_distances(self):
        return self.distances

    def get_shortest_paths(self):
        return self.paths

    def run_example(self, start_vertex):
        self.find_shortest_paths(start_vertex)

        shortest_distances = self.get_shortest_distances()
        shortest_paths = self.get_shortest_paths()

        print(f"Shortest distances from vertex {start_vertex}:")
        for vertex, distance in shortest_distances.items():
            print(f"To {vertex}: {distance}, Path: {shortest_paths[vertex]}")

graph = {
    '1':[('2', 4), ('3', 6), ('4', 6)],
    '2':[('3', 1), ('5', 7)],
    '3':[('5', 6), ('6', 4)],
    '4':[('3', 2), ('6', 5)],
    '5':[('7', 6)],
    '6':[('5', 1), ('7', 8)],
    '7':[]
}
graph2 = {
    '1':[('2', 1), ('3', 3)],
    '2':[('3', 1), ('4', 5), ('5', 3)],
    '3':[('5', 1), ('6', 4)],
    '4':[('5', 3), ('7', 8)],
    '5':[('6', 4), ('7', 7)],
    '6':[('8', 7)],
    '7':[('6', 6), ('8', 2)],
    '8':[]
}
graph3 ={
    'a':[('b', 2), ('c', 1)],
    'b':[('d', 2), ('e', 2), ('f', 5)],
    'c':[('b', 2), ('d', 2), ('e', 2)],
    'd':[('f', 3), ('g', 7)],
    'e':[('d', 3), ('f', 6), ('g', 8)],
    'f':[('g', 5), ('h', 2)],
    'g':[('h', 6)],
    'h':[]
}
graph4 ={
    'v1':[('v2', 7), ('v3', 4), ('v4', 6), ('v5', 1)],
    'v2':[],
    'v3':[('v2', 2), ('v4', 5)],
    'v4':[('v2', 3)],
    'v5':[('v4', 1)]

}

graph5 ={
    'v0':[('v1', 4), ('v7', 8)],
    'v1':[('v0', 4), ('v7', 11), ('v2', 8)],
    'v2':[('v1', 8), ('v3', 7), ('v5', 4), ('v8', 2)],
    'v3':[('v2', 7), ('v4', 9), ('v5', 14)],
    'v4':[('v3', 9), ('v5', 10)],
    'v5':[('v3', 14), ('v4', 10), ('v6', 2)],
    'v6':[('v5', 2), ('v7', 1), ('v8', 6)],
    'v7':[('v0', 8), ('v1', 11), ('v6', 1), ('v8', 7)],
    'v8':[('v2', 2),('v6', 6), ('v7', 7)]
}



start_vertex = 'v0'
dijkstra_instance = Dijkstra(graph5)
dijkstra_instance.run_example(start_vertex)