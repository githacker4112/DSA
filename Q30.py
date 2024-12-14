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

    # Perform DFS traversal starting from the given node
    def dfs(self, start):
        # Create a set to store visited nodes
        visited = set()
        
        # Call the recursive DFS helper function
        self._dfs_recursive(start, visited)

    # Helper function for recursive DFS
    def _dfs_recursive(self, node, visited):
        # Mark the node as visited
        visited.add(node)
        print(node, end=" ")

        # Visit all the unvisited neighbors of the current node
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

# Driver code to test the Graph and DFS implementation
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

    # Perform DFS traversal starting from node 1
    print("Depth First Search (DFS) starting from node 1:")
    g.dfs(1)
