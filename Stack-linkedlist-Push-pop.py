class Node:
    def __init__(self, data):
        self.data = data  # Data for the node
        self.next = None  # Reference to the next node (initialized as None)

class Stack:
    def __init__(self):
        self.top = None  # Initialize the top of the stack as None (empty stack)

    def is_empty(self):
        # Check if the stack is empty (top is None)
        return self.top is None

    def push(self, data):
        # Push a new element onto the stack
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.top  # Make the new node's next point to the current top
        self.top = new_node  # Update the top to the new node

        print(f"Pushed {data} onto stack.")

    def pop(self):
        # Pop the top element from the stack
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
        else:
            popped_node = self.top  # The node to be popped is the current top node
            self.top = self.top.next  # Update the top to the next node
            print(f"Popped {popped_node.data} from stack.")
            del popped_node  # Delete the popped node to free memory

    def display(self):
        # Display the stack from top to bottom
        if self.is_empty():
            print("Stack is empty.")
        else:
            temp = self.top
            print("Stack (top to bottom):")
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

# Menu-driven program
def menu():
    stack = Stack()

    while True:
        print("\nMenu:")
        print("1. Push an element onto the stack")
        print("2. Pop an element from the stack")
        print("3. Display the stack")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter the data to push onto the stack: ")
            stack.push(data)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
