class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
ll = LinkedList()

n = int(input("Enter the number of values to insert: "))
for _ in range(n):
    value = int(input("Enter a value: "))
    ll.insert(value)

while True:
    action = input("Enter 'i' to insert, 'd' to delete, 's' to search, or 'q' to quit: ")

    if action == 'i':
        value = int(input("Enter the value to insert: "))
        ll.insert(value)
        print(f"{value} has been inserted.")

    elif action == 'd':
        value = int(input("Enter the value to delete: "))
        ll.delete(value)
        print(f"{value} has been deleted.")

    elif action == 's':
        value = int(input("Enter the value to search for: "))
        found = ll.search(value)
        if found:
            print(f"{value} is in the linked list.")
        else:
            print(f"{value} is not in the linked list.")

    elif action == 'q':
        print("Exiting the program.")
        break

else:
    print("Invalid input.")

