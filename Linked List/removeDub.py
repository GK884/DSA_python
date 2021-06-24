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

# Remove Dublicates from the linked list


#Using temp set for storing values
# time complexity--> 0(n)
#space complexity--> 0(n)
def removedublicates(arglist):
    if arglist.head == None:
        return 'empty list'
    else:
        node = arglist.head
        values = set([node.value])
        while node.next:
            if node.next.value in values:
                node.next = node.next.next
            else:
                values.add(node.value)
                node = node.next
    return arglist


# Without using temp set
# Time Complexity-->  0(n^2)
# Space Complexity--> 0(1)

def removedublicates1(arglist):
    if arglist.head == None:
        return 'Empty list'
    else:
        node = arglist.head
        while node:
            nextnode = node
            while nextnode.next:
                if nextnode.next.value == node.value:
                    nextnode.next = nextnode.next.next
                else:
                    nextnode = nextnode.next
            node = node.next
    return 0

customll = LinkedList()
customll.generate_random(10,0,99)
print(customll)
print(len(customll))
removedublicates1(customll)
print(customll)
print(len(customll))