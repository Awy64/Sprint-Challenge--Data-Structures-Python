from stack import Stack
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

    def reverse_list(self, node, prev):
        if self.head == None:
            return
        stack = Stack()
        stack.push(self.head)
        current = self.head
        current = current.get_next()
        while current:
            stack.push(current)
            current = current.get_next()
        cur = stack.pop()
        self.head = cur
        while stack.size != 0:
            cur.set_next(stack.pop())
            cur = cur.next_node
        if stack.size == 0 and cur.next_node:
            cur.next_node = None

