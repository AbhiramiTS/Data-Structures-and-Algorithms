import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        # Create a new LinkedList for each test
        self.linked_list = LinkedList(1)

    def test_initialization(self):
        # Test if the LinkedList is initialized correctly
        self.assertEqual(self.linked_list.head.value, 1)
        self.assertEqual(self.linked_list.tail.value, 1)
        self.assertEqual(self.linked_list.length, 1)

    def test_append(self):
        # Test appending a new node to the LinkedList
        self.linked_list.append(2)
        self.assertEqual(self.linked_list.head.value, 1)
        self.assertEqual(self.linked_list.tail.value, 2)
        self.assertEqual(self.linked_list.length, 2)

        # Test appending more nodes
        self.linked_list.append(3)
        self.linked_list.append(4)
        self.assertEqual(self.linked_list.head.value, 1)
        self.assertEqual(self.linked_list.tail.value, 4)
        self.assertEqual(self.linked_list.length, 4)

    def test_print(self):
        # Test the print method of the LinkedList
        self.linked_list.append(2)
        self.linked_list.append(3)

        # Redirect stdout to capture print output
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        self.linked_list.print()

        # Get the printed value
        printed_value = sys.stdout.getvalue().strip()

        # Reset redirect.
        sys.stdout = original_stdout

        self.assertEqual(printed_value, "1 2 3")

    def test_list_not_empty(self):
        # Test if the list_not_empty method works correctly
        self.assertTrue(self.linked_list.list_not_empty())
        self.linked_list.pop()
        self.assertFalse(self.linked_list.list_not_empty())

    def test_is_valid_index(self):
        # Test if the is_valid_index method works correctly
        self.assertTrue(self.linked_list.is_valid_index(0))
        # self.assertTrue(self.linked_list.is_valid_index(1))  # Test for index 1
        # self.assertFalse(self.linked_list.is_valid_index(2))

    def test_pop(self):
        # Test the pop method
        self.assertEqual(self.linked_list.pop().value, 1)
        self.assertEqual(self.linked_list.length, 0)
        self.assertIsNone(self.linked_list.pop())

    def test_prepend(self):
        # Test the prepend method
        self.linked_list.prepend(2)
        self.assertEqual(self.linked_list.head.value, 2)
        self.assertEqual(self.linked_list.tail.value, 1)
        # print(self.linked_list.length)
        self.assertEqual(self.linked_list.length, 2)

        self.linked_list.prepend(3)
        self.assertEqual(self.linked_list.head.value, 3)
        self.assertEqual(self.linked_list.tail.value, 1)
        self.assertEqual(self.linked_list.length, 3)

    def test_pop_first(self):
        # Test the pop_first method
        self.assertEqual(self.linked_list.pop_first().value, 1)
        self.assertEqual(self.linked_list.length, 0)
        self.assertIsNone(self.linked_list.pop_first())

    def test_get(self):
        # Test the get method
        self.linked_list.append(2)
        self.linked_list.append(3)

        self.assertEqual(self.linked_list.get(0).value, 1)
        self.assertEqual(self.linked_list.get(1).value, 2)
        self.assertEqual(self.linked_list.get(2).value, 3)

        # Test for an invalid index
        self.assertIsNone(self.linked_list.get(3))

    def test_set(self):
        # Test the set method
        self.linked_list.set(0, 10)
        self.assertEqual(self.linked_list.head.value, 10)
        self.assertEqual(self.linked_list.length, 1)

        self.linked_list.append(2)
        self.linked_list.append(3)

        self.assertTrue(self.linked_list.set(1, 20))
        self.assertEqual(self.linked_list.get(1).value, 20)

        # Test for an invalid index
        self.assertFalse(self.linked_list.set(3, 30))

    def test_insert(self):
        print(self.linked_list.length)
        # Test the insert method
        self.linked_list.insert(0, 10)
        self.assertEqual(self.linked_list.head.value, 10)
        self.assertEqual(self.linked_list.length, 2)

        self.linked_list.append(20)
        self.linked_list.append(30)

        self.assertTrue(self.linked_list.insert(1, 15))
        self.assertEqual(self.linked_list.get(1).value, 15)

        # Test for an invalid index
        self.assertIsNone(self.linked_list.insert(6, 40))

    def test_remove(self):
        # Test the remove method
        self.linked_list.remove(0)
        self.assertEqual(self.linked_list.head, None)
        self.assertEqual(self.linked_list.length, 0)

        self.linked_list.append(10)
        self.linked_list.append(20)
        self.linked_list.append(30)

        removed_node = self.linked_list.remove(1)
        self.assertEqual(removed_node.value, 20)
        self.assertEqual(self.linked_list.get(1).value, 30)
        self.assertEqual(self.linked_list.length, 2)

        # Test for an invalid index
        self.assertIsNone(self.linked_list.remove(3))


if __name__ == '__main__':
    unittest.main()
