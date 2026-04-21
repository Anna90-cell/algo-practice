# Stack
# Last In First Out (LIFO) data structure

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack (top -> bottom):", self.items[::-1])

# Test
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("After pushing 1, 2, 3:")
    s.display()
    print("Peek:", s.peek())
    print("Pop:", s.pop())
    print("After popping:")
    s.display()
