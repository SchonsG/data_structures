class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head

        node = starting_point

        while node and (node.next != starting_point):
            yield node
            node = node.next

        yield node

    def print_list(self, starting_point=None):
        nodes = []

        for node in self.traverse(starting_point):
            nodes.append(str(node))

        print(" -> ".join(nodes))

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

if __name__ == "__main__":
    my_circular_list = CircularLinkedList()

    a = Node("a")
    b = Node("b")
    c = Node("c")

    a.next = b
    b.next = c
    c.next = a

    my_circular_list.head = a
    my_circular_list.print_list()

    my_circular_list.print_list(c)

