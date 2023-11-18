''' 
Sorted Insert in a Singly Linked List 

I/P : 10 -> 20 -> 30 -> 40 -> 50
      x = 25
O/P : 10 -> 20 -> 25 -> 30 -> 40 -> 50

I/P : 10 -> 20 -> 25 
      x = 5
O/P : 5 -> 10 -> 20 -> 25

I/P : 10 -> 20
      x = 30
O/P : 5 -> 10 -> 20 -> 30

'''

from main import LinkedList, Node

class SortedInsert(LinkedList):

    def __init__(self, value):
        super().__init__(value)
        self.append(20)
        self.append(30)
        self.append(40)
        self.append(50)
    
    def insert(self, num):
        node = Node(num)
        temp = self.head
        if temp is None:
            self.head = self.tail = node
        elif node.value < temp.value:
            node.next = self.head
            self.head = node
        else:
            while temp.next is not None and temp.next.value < node.value:
                temp = temp.next
            node.next = temp.next
            temp.next = node
            self.length += 1
        self.print()

new_node = SortedInsert(10)
user_input = input("Enter the number to be inserted in the sorted array: ")
new_node.insert(int(user_input))

        









