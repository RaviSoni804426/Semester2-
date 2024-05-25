class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.size > 0

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def __str__(self):
        return " -> ".join(str(item) for item in self)

    def _get_node_at(self, index):
        assert index >= 0 and index < self.size
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def insert(self, index, element):
        assert index >= 0 and index <= self.size
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = self._get_node_at(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def delete(self, index):
        assert index >= 0 and index < self.size
        if index == 0:
            curr = self.head
            self.head = self.head.next
            del curr
        else:
            prev = self._get_node_at(index - 1)
            curr = prev.next
            prev.next = prev.next.next
            del curr
        self.size -= 1

    def rotate(self, k):
        assert k >= 0 and k < self.size
        steps = k % self.size
        if steps == 0:
            return
        new_head = self._get_node_at(self.size - steps)
        temp = new_head.next
        new_head.next = None
        self.tail().next = self.head
        self.head = temp

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
        else:
            self.tail().next = new_node
        self.size += 1

    def prepend(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def merge(self, other):
        if not other:
            return
        if not self.head:
            self.head = other.head
        else:
            self.tail().next = other.head
        self.size += len(other)
        other.clear()

    def interleave(self, other):
        if not other:
            return
        curr = self.head
        other_head = other.head
        while curr and other_head:
            next_node = curr.next
            other_next = other_head.next
            curr.next = other_head
            other_head.next = next_node
            curr = next_node
            other_head = other_next
        if curr:
            self.tail().next = other_head
        else:
            self.head = other_head
        self.size += len(other)
        other.clear()

    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def index(self, element):
        for i, node in enumerate(self):
            if node == element:
                return i
        return 