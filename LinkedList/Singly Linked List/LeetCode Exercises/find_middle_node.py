'''
LL: Find Middle Node ( ** Interview Question)

Implement the find_middle_node method for the LinkedList class.

The find_middle_node method should return the middle node in the linked list WITHOUT using the length attribute.

If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:

The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.

When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.

The method should return the middle node or the first node of the second half of the list if the list has an even number of nodes.

The method should only traverse the linked list once.  In other words, you can only use one loop.

'''

from main import LinkedList

class FindMiddle(LinkedList):

    def __init__(self, value):
        super().__init__(value)

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print(slow.value)


if __name__ == "__main__":
    new_node = FindMiddle(10)
    items = [5, 20, 15, 25]
    for i in items:
        new_node.append(i)
    new_node.find_middle()


"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""