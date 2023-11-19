'''
Segregate Even and Odd Nodes

i/p: 17 -> 15 -> 8 -> 12 -> 5
o/p: 8 -> 12 -> 17 -> 15 -> 5

i/p: 8 -> 12 -> 10
o/p: 8 -> 12 -> 10

i/p: 3 -> 5 -> 1
o/p: 3 -> 5 -> 1

'''
from main import LinkedList

class EvenOdd(LinkedList):

    def __init__(self, value):
        super().__init__(value)

    def segregate(self):
        even_ptr = self.head
        odd_ptr = self.tail

        while even_ptr is not None or even_ptr.next is not None:
            if even_ptr.next.value % 2 != 0:
                self.head = self.head.next
                temp = even_ptr.next
                even_ptr.next = temp.next
                temp.next = None
                odd_ptr.next = temp
                odd_ptr = temp
            else:
                even_ptr = even_ptr.next




if __name__ == "__main__":
    new_node = EvenOdd(10)
    items = [17, 15, 8, 12, 5]
    for i in items:
        new_node.append(i)
    print("Elements before sorting: ")
    new_node.print()
    new_node.segregate()
    print("Elements after Sorting :")
    new_node.print()
