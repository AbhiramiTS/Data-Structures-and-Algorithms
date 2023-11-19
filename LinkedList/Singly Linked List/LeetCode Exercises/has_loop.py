'''
LL: Has Loop ( ** Interview Question)

Write a method called has_loop that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.

The method should follow these guidelines:


# HINTS

Create two pointers, slow and fast, both initially pointing to the head of the linked list.

Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.

If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.

If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.

'''

from main import LinkedList


class HasLoop(LinkedList):

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
            # Remove the loop 
            slow = self.head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

            fast.next = None


if __name__ == "__main__":
    new_node = HasLoop(1)
    items = [5, 20, 15, 25, 30]
    for i in items:
        new_node.append(i)
    new_node.print()
    new_node.create_loop()
    # Uncomment the code below to display the linked list that includes a loop.
    # new_node.print()
    new_node.detect_loop()
    new_node.print()