from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.marker = None

    def append(self, item):
        if len(self.storage) == 0:
            self.storage.add_to_head(item)
            self.marker = self.storage.head
            return
        elif len(self.storage) < self.capacity:
            self.marker.insert_after(item)
            self.marker = self.marker.next
            self.storage.length += 1
            if len(self.storage) == self.capacity:
                self.marker = self.storage.head
            return
        elif len(self.storage) == self.capacity:
            self.marker.insert_before(item)
            if self.storage.head is self.marker:
                self.storage.head = self.marker.prev
                temp_val = self.marker
                self.marker.delete()
                self.marker = temp_val.next
            elif self.marker.next is None:
                temp_val = self.marker
                self.marker = self.storage.head
                temp_val.delete()
            else:
                temp_val = self.marker
                self.marker = self.marker.next
                temp_val.delete()

    def get(self):
        lister = []
        if len(self.storage) != 0:
            current_node = self.storage.head
            while current_node is not None:
                lister.append(current_node.value)
                current_node = current_node.next
        return lister


# xer = RingBuffer(4)
# xer.append(1)
# print(xer.get())
# print('marker', xer.marker.value, 'head', xer.storage.head.value)
# xer.append(2)
# print(xer.get())
# print('marker', xer.marker.value, 'head', xer.storage.head.value)
# xer.append(3)
# print(xer.get())
# print('marker', xer.marker.value, 'head', xer.storage.head.value)
# xer.append(4)
# print(xer.get())
# print('marker', xer.marker.value, 'head', xer.storage.head.value)
# xer.append(5)
# print(xer.get())
# print('marker', xer.marker.value, 'head', xer.storage.head.value)
# xer.append(6)
# print(xer.get())
# print('marker', xer.marker.value, 'head', xer.storage.head.value)
# xer.append(7)
# print(xer.get())
# print('marker', xer.marker.value, 'head', xer.storage.head.value)
# xer.append(8)
# print(xer.get())
# print('marker', xer.marker.value, 'head', xer.storage.head.value)
# xer.append(9)
# print(xer.get())
# print('marker', xer.marker.value, 'head', xer.storage.head.value)
# xer.append(10)
# print(xer.get())
# print('marker', xer.marker.value, 'head', xer.storage.head.value)
