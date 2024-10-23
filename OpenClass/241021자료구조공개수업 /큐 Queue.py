class Queue:
    def __init__(self):
        self.queue = []
   
    def enqueue(self, value):
        self.queue.append(value)
        print(f"{value} has been added to the queue.")
   
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        value = self.queue.pop(0)
        print(f"{value} has been removed from the queue.")
        return value
   
    def peek(self):
        if self.is_empty():
            print("Queue is empty. No front element.")
            return None
        return self.queue[0]
   
    def is_empty(self):
        return len(self.queue) == 0
   
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue (front to back): " + " -> ".join(map(str, self.queue)))

# 사용자 입력 예시
q = Queue()

while True:
    action = input("Enter 'e' to enqueue, 'd' to dequeue, 'v' to view front, 'dis' to display queue, or 'q' to quit: ")
   
    if action == 'e':
        value = int(input("Enter the value to enqueue: "))
        q.enqueue(value)
       
    elif action == 'd':
        q.dequeue()
       
    elif action == 'v':
        front = q.peek()
        if front is not None:
            print(f"Front element is: {front}")
   
    elif action == 'dis':
        q.display()
   
    elif action == 'q':
        print("Exiting the program.")
        break
   
    else:
        print("Invalid input.")
