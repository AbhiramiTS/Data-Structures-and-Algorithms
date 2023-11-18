
from linked_list import LinkedList
from search import search

def recursive_linkedlist(obj):
    if obj is None:
        return
    print(obj.value)
    recursive_linkedlist(obj.next)

if __name__ == "__main__":
    new_node = LinkedList(1)
    new_node.append(2)
    new_node.append(3)
    new_node.append(4)
    new_node.append(5)
    
    recursive_linkedlist(new_node.head)
    search_position = search(new_node.head, 4)
    print(search_position)

