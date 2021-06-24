from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '-> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        return self.tail

    def generate_random(self, n, min_val, max_val):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_val, max_val))
        return self


newlink = LinkedList()
newlink.generate_random(11, 0, 99)
print(newlink)
print(len(newlink))
newlink.add(33)
print(newlink)