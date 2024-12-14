class Stack:
    def __init__(self, size):
        # Initialize the stack with a given size
        self.stack = []
        self.size = size

    def is_full(self):
        # Check if the stack is full
        return len(self.stack) == self.size

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def push(self, char):
        # Push a character to the stack if it's not full
        if self.is_full():
            print("Stack is full! Cannot push.")
        else:
            self.stack.append(char)
            print(f"Pushed {char} to stack.")

    def pop(self):
        # Pop a character from the stack if it's not empty
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
        else:
            char = self.stack.pop()
            print(f"Popped {char.upper()} from stack.")  # Convert to uppercase before printing

    def display(self):
        # Display the current contents of the stack
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Current stack (top to bottom):")
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i], end=" ")
            print()

# Menu-driven program
def menu():
    stack_size = int(input("Enter the size of the stack: "))
    stack = Stack(stack_size)

    while True:
        print("\nMenu:")
        print("1. Push a lowercase character to the stack")
        print("2. Pop a character from the stack (convert to uppercase)")
        print("3. Display the stack")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            if not stack.is_full():
                char = input("Enter a lowercase character to push: ").lower()
                if char.isalpha() and len(char) == 1 and char.islower():
                    stack.push(char)
                else:
                    print("Invalid input! Please enter a lowercase character.")
            else:
                print("Stack is full! Cannot push more items.")
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.display()  # Call the display function to show the current stack
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
