from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if self.value > value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif self.value < target:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    def get_max(self):
        max_val = self.value
        if self.right:
            return self.right.get_max()
        else:
            return max_val

    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    def in_order_print(self, node):
        if node == None:
            return
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    def bft_print(self, node):
        q = deque()
        q.append(self)
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            print(current_node.value)

    def dft_print(self, node):
        q = []
        q.append(node)
        while len(q) > 0:
            current_node = q.pop()
            if current_node.right:
                q.append(current_node.right)
            if current_node.left:
                q.append(current_node.left)
            print(current_node.value)

    def pre_order_dft(self, node):
        if node == None:
            return
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)

    def post_order_dft(self, node):
        if node == None:
            return
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)
