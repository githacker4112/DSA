class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node

class Queue:
    def __init__(self):
        self.front = None  # Front of the queue
        self.rear = None   # Rear of the queue

    # Function to check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Function to insert (enqueue) an element into the queue
    def insert(self, data):
        new_node = Node(data)  # Create a new node with the given data
        
        if self.is_empty():
            self.front = self.rear = new_node  # If queue is empty, both front and rear will point to the new node
        else:
            self.rear.next = new_node  # Attach the new node at the rear
            self.rear = new_node  # Update the rear pointer
        print(f"Inserted {data} into the queue.")

    # Function to delete (dequeue) an element from the queue
    def delete(self):
        if self.is_empty():
            print("Queue is empty! Cannot delete.")
        else:
            removed_data = self.front.data  # Get the front element
            print(f"Deleted {removed_data} from the queue.")
            self.front = self.front.next  # Move the front pointer to the next node

            # If the queue becomes empty after deletion, set rear to None
            if self.front is None:
                self.rear = None

    # Function to display the elements of the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            temp = self.front
            print("Queue elements are: ", end="")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

# Driver code
if __name__ == "__main__":
    queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Insert (Enqueue)")
        print("2. Delete (Dequeue)")
        print("3. Display Queue")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter the data to insert: "))
            queue.insert(data)
        elif choice == 2:
            queue.delete()
        elif choice == 3:
            queue.display()
        elif choice == 4:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")
