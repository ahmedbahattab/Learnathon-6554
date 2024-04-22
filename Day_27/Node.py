class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        prev_node = None
        current_node = self.head
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if not current_node:
            return

        prev_node.next = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
if __name__ == "__main__":
    # Creating a new linked list
    linked_list = LinkedList()

    # Inserting elements
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.append(15)

    # Displaying the linked list
    linked_list.display()  # Output: 10 -> 5 -> 15 -> None

    # Deleting an element
    linked_list.delete(5)

    # Displaying the modified linked list
    linked_list.display()  # Output: 10 -> 15 -> None
