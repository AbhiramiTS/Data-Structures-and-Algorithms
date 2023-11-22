'''
Middle of the Linked List

i/p : 10 -> 5 -> 20 -> 15 -> 25
o/p : 20

i/p : 10 -> 5 -> 20 -> 15 -> 25 -> 30
o/p : 15

i/p : 10
o/p : 10

i/p : None
o/p : 

i/p : 10 -> 20
o/p : 20

'''

from main import LinkedList, Node

class Middle(LinkedList):

    def __init__(self, value):
        super().__init__(value)

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print(slow.value)


new_node = Middle(10)
items = [5, 20, 15, 25, 30]
for i in items:
    new_node.append(i)
new_node.find_middle()
