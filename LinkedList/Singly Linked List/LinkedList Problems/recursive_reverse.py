from main import LinkedList

class RecursiveReverse(LinkedList):

    def __init__(self, value):
        super().__init__(value)

    def reverse(self, curr, next, prev):

        if prev == None:
            # TODO
            return 