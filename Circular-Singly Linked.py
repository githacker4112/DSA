class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.start = None
        self.temp = None

    def create(self):
        data = int(input("Get information for new node: "))
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            self.start.next = self.start  # The next of the last node points to the start (circular link)
        else:
            self.temp = self.start
            while self.temp.next != self.start:
                self.temp = self.temp.next
            self.temp.next = new_node
            new_node.next = self.start  # The new node points back to the start (circular link)

    def show(self):
        if self.start is None:
            print("CSLL does not exist")
        else:
            self.temp = self.start
            while True:
                print(self.temp.data, end="->")
                self.temp = self.temp.next
                if self.temp == self.start:
                    break
            print("... (Circular)")

    def insert(self):
        if self.start is None:
            print("CSLL does not exist")
        else:
            data = int(input("Get information for new node: "))
            new_node = Node(data)
            pos = int(input("Get position for new node: "))
            if pos == 1:
                new_node.next = self.start
                self.temp = self.start
                while self.temp.next != self.start:
                    self.temp = self.temp.next
                self.temp.next = new_node
                self.start = new_node
            else:
                c = 1
                self.temp = self.start
                while c != pos - 1:
                    self.temp = self.temp.next
                    c += 1
                new_node.next = self.temp.next
                self.temp.next = new_node

    def delete(self):
        if self.start is None:
            print("CSLL does not exist")
        else:
            pos = int(input("Get position of the node to delete: "))
            if pos == 1:
                if self.start.next == self.start:  # Only one node
                    self.start = None
                else:
                    self.temp = self.start
                    while self.temp.next != self.start:
                        self.temp = self.temp.next
                    self.start = self.start.next
                    self.temp.next = self.start
            else:
                c = 1
                self.temp = self.start
                while c != pos - 1:
                    self.temp = self.temp.next
                    c += 1
                self.temp.next = self.temp.next.next

    def search(self):
        if self.start is None:
            print("CSLL does not exist")
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
    csObj = CircularSinglyLinkedList()
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
            csObj.create()
        elif choice == 2:
            csObj.insert()
        elif choice == 3:
            csObj.delete()
        elif choice == 4:
            csObj.search()
        elif choice == 5:
            csObj.show()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
