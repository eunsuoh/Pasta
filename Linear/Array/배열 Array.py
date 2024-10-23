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
    
