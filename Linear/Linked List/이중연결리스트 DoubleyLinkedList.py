class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete_node(self, key):
        cur_node = self.head

        while cur_node:
            if cur_node.data == key:
                if cur_node.prev:
                    cur_node.prev.next = cur_node.next
                if cur_node.next:
                    cur_node.next.prev = cur_node.prev
                if cur_node == self.head:
                    self.head = cur_node.next
                cur_node = None
                return
            cur_node = cur_node.next

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

# 사용 예제
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append("A")
doubly_linked_list.append("B")
doubly_linked_list.append("C")
doubly_linked_list.prepend("D")
doubly_linked_list.print_list()
print("After deleting an element:")
doubly_linked_list.delete_node("B")
doubly_linked_list.print_list()
