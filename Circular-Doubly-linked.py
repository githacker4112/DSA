class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.start = None
        self.temp = None

    def create(self):
        data = int(input("Get information for new node: "))
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            self.start.next = self.start  # The next of the last node points to the start (circular link)
            self.start.prev = self.start  # The prev of the start node points to itself (circular link)
        else:
            self.temp = self.start
            while self.temp.next != self.start:  # Traverse till the last node
                self.temp = self.temp.next
            self.temp.next = new_node
            new_node.prev = self.temp
            new_node.next = self.start
            self.start.prev = new_node  # Make the start's prev point to the new node

    def show(self):
        if self.start is None:
            print("CDLL does not exist")
        else:
            self.temp = self.start
            while True:
                print(self.temp.data, end="<->")
                self.temp = self.temp.next
                if self.temp == self.start:  # Loop back to start when we reach the end
                    break
            print("... (Circular)")

    def insert(self):
        if self.start is None:
            print("CDLL does not exist")
        else:
            data = int(input("Get information for new node: "))
            new_node = Node(data)
            pos = int(input("Get position for new node: "))
            if pos == 1:
                new_node.next = self.start
                new_node.prev = self.start.prev
                self.start.prev.next = new_node
                self.start.prev = new_node
                self.start = new_node
            else:
                c = 1
                self.temp = self.start
                while c != pos - 1:
                    self.temp = self.temp.next
                    c += 1
                new_node.next = self.temp.next
                if self.temp.next != self.start:
                    self.temp.next.prev = new_node
                new_node.prev = self.temp
                self.temp.next = new_node

    def delete(self):
        if self.start is None:
            print("CDLL does not exist")
        else:
            pos = int(input("Get position of the node to delete: "))
            if pos == 1:
                if self.start.next == self.start:  # Only one node
                    self.start = None
                else:
                    self.start.next.prev = self.start.prev
                    self.start.prev.next = self.start.next
                    self.start = self.start.next
            else:
                c = 1
                self.temp = self.start
                while c != pos - 1:
                    self.temp = self.temp.next
                    c += 1
                node_to_delete = self.temp.next
                self.temp.next = node_to_delete.next
                if node_to_delete.next != self.start:
                    node_to_delete.next.prev = self.temp
                node_to_delete = None

    def search(self):
        if self.start is None:
            print("CDLL does not exist")
        else:
            data = int(input("Enter the value to search: "))
            self.temp = self.start
            index = 1
            while True:
                if self.temp.data == data:
                    print(f"Value {data} found at index {index}.")
                    return
                self.temp = self.temp.next
                index += 1
                if self.temp == self.start:
                    break
            print(f"Value {data} not found in the list.")

# Menu-driven program
def menu():
    cdObj = CircularDoublyLinkedList()
    while True:
        print("\nMenu:")
        print("1. Create a new node")
        print("2. Insert a node")
        print("3. Delete a node")
        print("4. Search for a node")
        print("5. Display the list")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            cdObj.create()
        elif choice == 2:
            cdObj.insert()
        elif choice == 3:
            cdObj.delete()
        elif choice == 4:
            cdObj.search()
        elif choice == 5:
            cdObj.show()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
