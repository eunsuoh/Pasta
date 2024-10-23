class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        if self.search(value):  # 중복 확인
            print(f"{value} is already in the linked list. Please enter a different value.")
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        if self.search(value):  # 중복 확인
            print(f"{value} is already in the linked list. Please enter a different value.")
            return
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_index(self, index, value):
        if self.search(value):  # 중복 확인
            print(f"{value} is already in the linked list. Please enter a different value.")
            return
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                print("Index out of bounds.")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

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

    def display(self):
        current = self.head
        if not current:
            print("The linked list is empty.")
            return
        print("Linked List: ", end="")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# 사용자 입력 예시
ll = LinkedList()

# Populate the linked list
n = int(input("Enter the number of values to insert: "))
for _ in range(n):
    while True:
        value = int(input("Enter a value: "))
        if not ll.search(value):  # 중복 확인
            ll.insert_at_end(value)  # Append at the end for demonstration
            break
        print(f"{value} is already in the linked list. Please enter a different value.")

while True:
    action = input("Enter 'i' to insert, 'd' to delete, 's' to search, 'dsp' to display, or 'q' to quit: ")
   
    if action == 'i':
        mode = input("Enter 'b' to insert at beginning, 'e' to insert at end, or 'idx' to insert at index: ")
        if mode == 'b':
            value = int(input("Enter the value to insert at the beginning: "))
            ll.insert_at_beginning(value)
        elif mode == 'e':
            value = int(input("Enter the value to insert at the end: "))
            ll.insert_at_end(value)
        elif mode == 'idx':
            index = int(input("Enter the index to insert at: "))
            value = int(input("Enter the value to insert: "))
            ll.insert_at_index(index, value)
   
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
   
    elif action == 'dsp':
        ll.display()
   
    elif action == 'q':
        print("Exiting the program.")
        break
   
    else:
        print("Invalid input.")
