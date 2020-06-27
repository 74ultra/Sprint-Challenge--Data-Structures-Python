class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def printer(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next_node

    def reverse_list(self, node, prev=None):
        if node is None:
            self.head = prev
            return
        if node is self.head and node.next_node is None:
            return node
        if node is not None:
            current_node = node
            next_one = current_node.next_node
            current_node.next_node = prev
            prev = current_node
            self.reverse_list(next_one, prev)


# xer = LinkedList()
# xer.add_to_head(1)
# xer.add_to_head(2)
# xer.add_to_head(3)
# xer.add_to_head(4)
# xer.add_to_head(5)

# xer.printer()
# xer.reverse_list(xer.head, None)

# xer.printer()
