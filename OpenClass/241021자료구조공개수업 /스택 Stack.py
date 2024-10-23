class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
        print(f"{value} has been pushed onto the stack.")
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        value = self.stack.pop()
        print(f"{value} has been popped from the stack.")
        return value
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty. No top element.")
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (top to bottom): " + " -> ".join(map(str, reversed(self.stack))))

# 사용자 입력 예시
s = Stack()

while True:
    action = input("Enter 'p' to push, 'o' to pop, 'v' to view top, 'd' to display stack, or 'q' to quit: ")
    
    if action == 'p':
        value = int(input("Enter the value to push: "))
        s.push(value)
        
    elif action == 'o':
        s.pop()
        
    elif action == 'v':
        top = s.peek()
        if top is not None:
            print(f"Top element is: {top}")
    
    elif action == 'd':
        s.display()
    
    elif action == 'q':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid input.")