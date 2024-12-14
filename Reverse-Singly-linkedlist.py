# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data  # stores the data of the node
        self.next = None  # pointer to the next node in the list

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.start = None  # initially the list is empty
        self.temp = None    # temporary variable for traversal
        self.prev = None    # previous node variable for operations

    # Function to add a new node at the end of the list (without using append)
    def insert_at_end(self, data):
        new_node = Node(data)  # create a new node with the given data
        
        if not self.start:  # If the list is empty, set the new node as the first node
            self.start = new_node
        else:
            self.temp = self.start
            while self.temp.next:  # Traverse to the last node
                self.temp = self.temp.next
            self.temp.next = new_node  # Attach the new node at the end

    # Function to traverse the linked list recursively and print elements in reverse order
    def traverse_reverse(self, node):
        if node is None:  # base case: if we reach the end of the list
            return
        self.traverse_reverse(node.next)  # recursive call to traverse the next node
        print(node.data, end=" -> ")  # print the current node data after returning from recursion

    # Function to initiate the recursive reverse traversal from the start node
    def reverse_traversal(self):
        if not self.start:  # check if the list is empty
            print("The list is empty.")
        else:
            self.traverse_reverse(self.start)
            print("None")  # to indicate the end of the list


# Creating the linked list
linked_list = SinglyLinkedList()

# Input the number of elements
n = int(input("Enter the number of elements you want to add to the list: "))

# Take input for the list from the user and insert each element at the end
for i in range(n):
    data = int(input(f"Enter data for node {i + 1}: "))
    linked_list.insert_at_end(data)

# Traversing the list in reverse order using recursion
print("\nTraversing the Singly Linked List in reverse order:")
linked_list.reverse_traversal()
