'''
Find nth node from the end of the Linked List

i/p : 10 -> 20 -> 30 -> 40 -> 50
n = 2
o/p :  40

i/p : 10 -> 20 -> 30
n = 3
o/p : 10

i/p : 10 -> 20
n = 3
o/p: 

'''

from main import LinkedList

class FindNode(LinkedList):

    def __init__(self, value):
        super().__init__(value)

    def find_node(self, position):
        first = self.head
        second = self.head
        for i in range(position):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        print(second.value)

new_node = FindNode(10)
items = [5, 20, 15, 25, 30, 40, 50]
for i in items:
    new_node.append(i)
new_node.find_node(7)
            


