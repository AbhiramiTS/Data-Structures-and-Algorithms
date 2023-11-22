'''
Delete node with the only pointer given to it.

     10 -> 20 -> 30 -> 40 -> 50 -> NULL
i/p: pointer or reference to the node 30

o/p: 10 -> 20 -> 40 -> 50

'''

from main import LinkedList
import random

class DeleteNode(LinkedList):

    def __init__(self, value):
        super().__init__(value)

    def get_random_node(self):
        temp = self.head
        index = random.randint(0, self.length - 1)
        for i in range(index):
            temp = temp.next
        return temp

    def delete(self, ptr):
        if ptr.next is not None:
            temp = ptr.next
            ptr.value = temp.value
            ptr.next = temp.next
            temp.next = None
        else:
            # when the element needs to be deleted is the last node
            self.pop()
            # ptr.next = None
            # ptr.value = None
        self.length -= 1

    
new_node = DeleteNode(10)
items = [5, 20, 15, 25, 30]
for i in items:
    new_node.append(i)
print("Items in the Linked List before deleting:")
new_node.print()
rand_node = new_node.get_random_node()
new_node.delete(rand_node)
print("\nItems in the Linked List after deleting:")
new_node.print()

