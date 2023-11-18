'''
Remove duplicates from a sorted linked list

i/p : 10, 20, 20, 30, 30, 30
o/p : 10, 20, 30

i/p: 5, 10, 15, 20
o/p : 5, 10, 15, 20

i/p: None
o/p : None

'''
from main import LinkedList


class RemoveDuplicates(LinkedList):

    def __init__(self, value):
        super().__init__(value)

    def remove(self):
        curr = self.head
        while curr is not None and curr.next is not None:
            if curr.value == curr.next.value:
                temp = curr.next
                curr.next = temp.next
                temp.next = None
            else:
                curr = curr.next
        

dup = RemoveDuplicates(10)
items = [10, 20, 20,20, 30, 30, 30]
for i in items:
    dup.append(i)
dup.remove()
dup.print()



