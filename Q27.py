# Node class to represent each node in the Binary Search Tree
class Node:
    def __init__(self, data):
        self.data = data  # Stores the data of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

# Binary Search Tree class
class BST:
    def __init__(self):
        self.root = None  # Initially, the tree is empty

    # Function to insert a new node into the BST
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node  # If the tree is empty, make this node the root
        else:
            self._insert_recursive(self.root, new_node)

    # Helper function for recursive insertion
    def _insert_recursive(self, root, new_node):
        # If data is less than root, go to the left subtree
        if new_node.data < root.data:
            if root.left is None:
                root.left = new_node  # Insert the new node here
            else:
                self._insert_recursive(root.left, new_node)  # Recurse on left subtree
        # If data is greater than root, go to the right subtree
        elif new_node.data > root.data:
            if root.right is None:
                root.right = new_node  # Insert the new node here
            else:
                self._insert_recursive(root.right, new_node)  # Recurse on right subtree

    # Function to perform In-Order traversal of the BST
    def in_order_traversal(self):
        if self.root is None:
            print("The tree is empty.")
        else:
            self._in_order_recursive(self.root)

    # Helper function for recursive In-Order traversal
    def _in_order_recursive(self, root):
        if root is not None:
            self._in_order_recursive(root.left)  # Traverse left subtree
            print(root.data, end=" ")  # Visit the root node
            self._in_order_recursive(root.right)  # Traverse right subtree

# Driver code to test the BST implementation
if __name__ == "__main__":
    bst = BST()

    # Get user input for the values to be inserted into the BST
    values = input("Enter values to insert into the BST (separated by spaces): ").split()

    # Insert each value into the BST
    for value in values:
        bst.insert(int(value))

    # Perform In-Order traversal and print the nodes
    print("In-Order Traversal of the BST:")
    bst.in_order_traversal()
