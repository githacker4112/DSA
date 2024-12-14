from collections import deque

# Class to represent a graph
class Graph:
    def __init__(self):
        # Initialize an empty graph
        self.graph = {}

    # Add a node to the graph
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    # Add an edge between two nodes
    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    # Perform BFS traversal starting from the given node
    def bfs(self, start):
        # Create a set to store visited nodes
        visited = set()
        # Create a queue to manage the BFS process
        queue = deque([start])

        # Mark the starting node as visited
        visited.add(start)

        # Perform BFS
        while queue:
            node = queue.popleft()  # Get the first node from the queue
            print(node, end=" ")

            # Visit all the neighbors of the current node
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Driver code to test the Graph and BFS implementation
if __name__ == "__main__":
    g = Graph()

    # Add nodes and edges
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)

    # Perform BFS traversal starting from node 1
    print("Breadth First Search (BFS) starting from node 1:")
    g.bfs(1)
