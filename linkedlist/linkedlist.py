class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class linkedlist:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        next_node = Node(data)
        if self.head is None:
            self.head = next_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = next_node

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        self.head = new_node
        new_node.next = current_node

    def remove(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            return
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        previous_node.next = current_node.next

    def reverse_iterative(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def reverse_recursive(self):
        def _reverse_recursive(current_node, previous_node):
            if not current_node:
                return previous_node
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)
        self.head = _reverse_recursive(self.head, None)

    def reverse_even(self):
        def _reverse_even(head, previous_node):
            if head is None:
                return None
            current_node = head
            while current_node and current_node.data % 2 == 0:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
            if current_node != head:
                head.next = current_node
                _reverse_even(current_node, None)
                return previous_node
            else:
                head.next = _reverse_even(head.next, head)
        self.head = _reverse_even(self.head, None)

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == '__main__':
    l = linkedlist()
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    l.print()
    print("---------------- Reverse Iter")
    l.reverse_iterative()
    l.print()
    print("---------------- Reverse Recursive")
    l.reverse_recursive()
    l.print()
    print("---------------- Reverse Even")
    l_2 = linkedlist()
    l_2.append(2)
    l_2.append(4)
    l_2.append(6)
    l_2.append(1)
    l_2.append(12)
    l_2.append(14)
    l_2.append(16)
    l_2.reverse_even()
    l_2.print()
