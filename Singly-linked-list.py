class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.start = None
        self.temp = None

    def create(self):
        data = int(input("Get information for new node: "))
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            self.temp = new_node
        else:
            self.temp.next = new_node
            self.temp = new_node

    def show(self):
        if self.start is None:
            print("SLL does not exist")
        else:
            self.temp = self.start
            while self.temp:
                print(self.temp.data, end="->")
                self.temp = self.temp.next
            print("None")

    def insert(self):
        if self.start is None:
            print("SLL does not exist")
        else:
            data = int(input("Get information for new node: "))
            new_node = Node(data)
            pos = int(input("Get position for new node: "))
            if pos == 1:
                new_node.next = self.start
                self.start = new_node
            else:
                c = 1
                self.temp = self.start
                while c != pos:
                    self.prev = self.temp
                    self.temp = self.temp.next
                    c += 1
                self.prev.next = new_node
                new_node.next = self.temp

    def delete(self):
        if self.start is None:
            print("SLL does not exist")
        else:
            pos = int(input("Get position of the node to delete: "))
            if pos == 1:
                self.start = self.start.next
            else:
                c = 1
                self.temp = self.start
                while c != pos:
                    self.prev = self.temp
                    self.temp = self.temp.next
                    c += 1
                self.prev.next = self.temp.next

    def search(self):
        if self.start is None:
            print("SLL does not exist")
        else:
            data = int(input("Enter the value to search: "))
            self.temp = self.start
            index = 1
            while self.temp:
                if self.temp.data == data:
                    print(f"Value {data} found at index {index}.")
                    return
                self.temp = self.temp.next
                index += 1
            print(f"Value {data} not found in the list.")

# Menu-driven program
def menu():
    sObj = SinglyLinkedList()
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
            sObj.create()
        elif choice == 2:
            sObj.insert()
        elif choice == 3:
            sObj.delete()
        elif choice == 4:
            sObj.search()
        elif choice == 5:
            sObj.show()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
