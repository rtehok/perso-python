class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.queue.move_to_front(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.queue.move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                evicted_key = self.queue.remove_last()
                del self.cache[evicted_key]
            new_node = DoublyLinkedListNode(key, value)
            self.cache[key] = new_node
            self.queue.add_first(new_node)


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def move_to_front(self, node):
        if node == self.head:
            return
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.add_first(node)

    def remove_last(self):
        if not self.tail:
            return None
        if self.head == self.tail:
            key = self.head.key
            self.head = None
            self.tail = None
        else:
            key = self.tail.key
            self.tail.prev.next = None
            self.tail = self.tail.prev
        return key


if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    assert obj.get(1) == 1
    obj.put(3, 3)
    assert obj.get(2) == -1
    obj.put(4, 4)
    assert obj.get(1) == -1
    assert obj.get(3) == 3
    assert obj.get(4) == 4
