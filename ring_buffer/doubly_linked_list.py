

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            current_head = self.head
            self.head = new_node
            self.head.next = current_head
            current_head.prev = self.head
            self.length += 1

    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            head_value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return head_value
        else:
            head_value = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return head_value

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            prev_tail = self.tail
            self.tail = new_node
            self.tail.prev = prev_tail
            prev_tail.next = self.tail
            self.length += 1

    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            removed_tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_tail.value
        else:
            removed_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return removed_tail.value

    def move_to_front(self, node):
        if self.head == node:
            return None
        if self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
            prev_head = self.head
            self.head = node
            prev_head.prev = self.head
            self.head.next = prev_head
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            prev_head = self.head
            self.head = node
            self.head.next = prev_head
            prev_head.prev = self.head
            self.head.prev = None

    def move_to_end(self, node):
        if self.tail is node:
            return None
        if self.head is node:
            self.head = self.head.next
            self.head.prev = None
            prev_tail = self.tail
            self.tail = node
            prev_tail.next = self.tail
            self.tail.prev = prev_tail
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            prev_tail = self.tail
            self.tail = node
            prev_tail.next = self.tail
            self.tail.prev = prev_tail
            self.tail.next = None

    def delete(self, node):
        if self.head is node and self.tail is node:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head is node:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
        elif self.tail is node:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.lenght -= 1

    def get_max(self):
        if self.head is None and self.tail is None:
            return None
        max_val = 0
        current_node = self.head
        while current_node is not None:
            if current_node.value > max_val:
                max_val = current_node.value
                current_node = current_node.next
            else:
                current_node = current_node.next
        return max_val
