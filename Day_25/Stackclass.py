class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def main():
    stack = Stack()

    # Push items onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Perform stack operations
    print("Size of stack:", stack.size())  # Output: 3
    print("Top of stack:", stack.peek())   # Output: 3

    # Pop an item from the stack
    item = stack.pop()
    print("Popped item:", item)            # Output: 3
    print("Size of stack after pop:", stack.size())  # Output: 2
    print("Is stack empty?", stack.is_empty())       # Output: False


if __name__ == "__main__":
    main()
