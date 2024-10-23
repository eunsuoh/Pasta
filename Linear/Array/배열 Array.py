class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def insert(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value

    def delete(self, index):
        if 0 <= index < self.size:
            self.array[index] = None

    def search(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1
    
size = int(input("Enter the size of the array: "))
arr = Array(size)

while True:
    action = input("Enter 'i' tp insert, 'd' to deleter, 's' to search, or 'q' to quit: ")

    if action == 'i':
        index = int(input("Enter the index to insert at: "))
        value = int(input("Enter the value to insert: "))
        arr.insert(index, value)
        print(f"{value} has been inserted at index {index}.")

    elif action == 'd':
        index = int(input("Enter the index to delete:"))
        arr.delete(index)
        print(f"The value at index {index} has been deleted.")

    elif action == 's':
        value = int(input("Enter the value to search for: "))
        index = arr.search(value)
        if index != -1:
            print(f"{value} is found at index {index}.")
        else:
            print(f"{value} is not in the array")

    elif action == 'q':
        print("Exiting the program.")
        break

    else:
        print("Invalid input.")