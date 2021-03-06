class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node

            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return

        for current_node in self:
            pass

        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head

        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return

            prev_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head

        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return

            prev_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    def reverse(self):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.next is None:
            return self

        values = []

        for node in self:
            values.append(node.data)

        values.reverse()

        reversed_linked_list = LinkedList(values)

        return reversed_linked_list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

if __name__ == "__main__":
    my_list = LinkedList(["b", "c"])
    print(my_list)

    for node in my_list:
        print(node)

    node = Node("a")
    my_list.add_first(node)
    print(my_list)

    node = Node("f")
    my_list.add_last(node)
    print(my_list)

    my_list.add_after("c", Node("d"))
    print(my_list)

    my_list.add_before("f", Node("e"))
    print(my_list)

    my_list.remove_node("f")
    print(my_list)

    print(my_list.reverse())

