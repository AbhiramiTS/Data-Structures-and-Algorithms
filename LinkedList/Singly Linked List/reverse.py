from linked_list import LinkedList


def reverse(linked_list):
    curr = linked_list.head
    prev = None
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    # Update the head of the linked list
    linked_list.head = prev

if __name__ == "__main__":

    new_node = LinkedList(1)
    new_node.append(2)
    new_node.append(3)
    new_node.append(4)
    new_node.append(5)
    
    reverse(new_node)
    new_node.print()
