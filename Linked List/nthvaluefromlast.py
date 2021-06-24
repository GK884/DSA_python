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


# Time Complexity --> 0(n)
# Space Complexity --> 0(1)

def findnth(arglist, n):
    if arglist.head == None:
        return 'Empty List'
    else:
        pt1 = arglist.head
        pt2 = arglist.head

        for i in range(n):
            if pt2 is None:
                return 'range is large'
            pt2 = pt2.next
        while pt2:
            pt2 = pt2.next
            pt1 = pt1.next
    return pt1.value


custom = LinkedList()
custom.generate_random(10, 0, 99)
print(custom)
print(len(custom))
print(findnth(custom, 5))