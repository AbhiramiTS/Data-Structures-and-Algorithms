class Node:
    def __init__(self, value):
        # Node constructor to initialize value and next pointer
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        # LinkedList constructor to initialize head, tail, and length
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print(self):
        # Print the elements in the linked list
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next


    def list_not_empty(self):
        # Check if the linked list is not empty
        return self.head is not None


    def is_valid_index(self, index):
        # Check if the given index is valid
        return 0 <= index < self.length


    def append(self, value):
        # Append a new node with the given value to the end of the linked list
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


    def pop(self):
        # Remove and return the last element from the linked list
        if self.list_not_empty():
            if self.head.next is None:
                pop_ele = self.head
                self.head = self.tail = None
            else:
                temp = self.head
                while temp.next is not self.tail:
                    temp = temp.next
                pop_ele = self.tail
                self.tail = temp
                self.tail.next = None
            self.length -= 1
            return pop_ele
        return None


    def prepend(self, value):
        # Add a new node with the given value to the beginning of the linked list
        new_node = Node(value)
        if not self.list_not_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


    def pop_first(self):
        # Remove and return the first element from the linked list
        if self.list_not_empty():
            temp = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            temp.next = None
            self.length -= 1
            return temp
        return None


    def get(self, index):
        # Get the node at the specified index
        if self.list_not_empty() and self.is_valid_index(index):
            temp = self.head
            for i in range(1, index + 1):
                temp = temp.next
            return temp
        return None


    def set(self, index, value):
        # Set the value of the node at the specified index
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


    def insert(self, index, value):
        # Insert a new node with the given value at the specified index
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        if temp:
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
        return None


    def remove(self, index):
        # Remove and return the node at the specified index
        if self.list_not_empty() and self.is_valid_index(index):
            if index == 0:
                removed_ele = self.pop_first()
            elif index == self.length - 1:
                removed_ele = self.pop()
            else:
                prev = self.get(index - 1)
                temp = prev.next
                removed_ele = temp
                prev.next = temp.next
                temp.next = None
                self.length -= 1
            return removed_ele


