class Queue:
    def __init__(self, size):
        self.size = size  # size of the queue
        self.queue = [None] * size  # create an array to represent the queue
        self.front = -1  # pointer to the front element
        self.rear = -1   # pointer to the rear element

    # Function to check if the queue is full
    def is_full(self):
        return self.rear == self.size - 1

    # Function to check if the queue is empty
    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    # Function to insert (enqueue) an element into the queue
    def insert(self, data):
        if self.is_full():
            print("Queue is full! Cannot insert.")
        else:
            if self.front == -1:  # If the queue is initially empty
                self.front = 0
            self.rear += 1  # move rear to the next position
            self.queue[self.rear] = data  # insert the element
            print(f"Inserted {data} into the queue.")

    # Function to delete (dequeue) an element from the queue
    def delete(self):
        if self.is_empty():
            print("Queue is empty! Cannot delete.")
        else:
            removed_data = self.queue[self.front]  # get the front element
            print(f"Deleted {removed_data} from the queue.")
            self.front += 1  # move front to the next element

            # If the queue becomes empty after deleting the last element
            if self.front > self.rear:
                self.front = self.rear = -1

    # Function to display the current elements in the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue elements are: ", end="")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

# Driver code
if __name__ == "__main__":
    size = int(input("Enter the size of the queue: "))
    queue = Queue(size)

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
