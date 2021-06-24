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


# Time Complextity --> 0(n)
# Space Comlexity --> 0(1)
def partition(arglist, x):
    node = arglist.head
    arglist.tail = node
    arglist.head = None

    while node:
        nextnode = node.next
        node.next = None
        if node.value < x:
            node.next = arglist.head
            arglist.head = node
        else:
            arglist.tail.next = node
            arglist.tail = node
        node = nextnode
    if arglist.tail.next is not None:
        arglist.tail.next = None

custom = LinkedList()
custom.generate_random(10, 0, 99)
print(custom)
print(len(custom))
partition(custom, 60)
print(custom)
