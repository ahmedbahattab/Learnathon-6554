class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

# Example usage:
q = Queue()
print("Is the queue empty?", q.is_empty())  # Output: True
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Queue size:", q.size())  # Output: 3
print("Front item:", q.peek())  # Output: 1
print("Dequeue:", q.dequeue())  # Output: 1
print("Queue size after dequeue:", q.size())  # Output: 2
print("Is the queue empty now?", q.is_empty())  # Output: False
