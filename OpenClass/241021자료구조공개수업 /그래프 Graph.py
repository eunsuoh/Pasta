class Graph:
    def __init__(self):
        self.graph = {}
        self.node_values = set()

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def build_graph(self):
        num_edges = int(input("Enter the number of edges: ")
        edges_added = 0

        while edges_added < num_edges:
            edge = input(f"Enter an edge (format: u v) for edge {edges_added +1}")
            u, v = edge.split()

            if u in self.node_values and v in self.node_values:
                print("Both nodes already exist! Please enter new nodes.")
                continue
                
            if u in self.node_values and v not in self.node_values:
                self.node_values.add(v)
            elif v in self.node_values and u not in self.node_values:
                self.node_values.add(u)
            else:
                self.node_values.add(u)
                self.node_values.add(v)

            self.add_edge(u, v)
            edges_added += 1

graph = Graph()
graph.build_graph()