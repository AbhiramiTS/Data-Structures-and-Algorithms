from main import LinkedList
from middle_of_linkedlist import Middle

class DetectLoop(LinkedList):

    def __init__(self, value):
        super().__init__(value)

    def create_loop(self):

        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        self.tail.next = slow 
        print(f"\nCreated a loop. Last Node {self.tail.value} now points to the middle node {slow.value}")


    def detect_loop(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if slow != fast:
            print("\nNo Loop detected!") 
        else:
            slow = self.head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

            fast.next = None


if __name__ == "__main__":
    new_node = DetectLoop(1)
    items = [5, 20, 15, 25, 30]
    for i in items:
        new_node.append(i)
    new_node.print()
    new_node.create_loop()
    # new_node.print()
    new_node.detect_loop()
    new_node.print()
    
    

    


        