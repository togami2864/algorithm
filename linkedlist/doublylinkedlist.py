class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        current_node.prev = new_node
        new_node.next = current_node
        self.head = new_node

    def remove(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return
        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            return

        if current_node.next is None:
            prev = current_node.prev
            prev.next = None
            current_node = None
            return
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == '__main__':
    d = DoublyLinkedList()
    d.append(1)
    d.append(2)
    d.append(3)
    d.insert(0)
    d.remove(0)
    d.print()
