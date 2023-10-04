class MyHashMapV1:

    def __init__(self):
        self.arr = [-1] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    def get(self, key: int) -> int:
        return self.arr[key]

    def remove(self, key: int) -> None:
        self.arr[key] = -1


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    def _index(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._index(key)
        if not self.table[idx]:
            self.table[idx] = ListNode(key, value)
            return

        curr = self.table[idx]

        while curr:
            if curr.key == key:
                curr.value = value
                return
            if not curr.next:
                curr.next = ListNode(key, value)
                return

            curr = curr.next

    def get(self, key: int) -> int:
        idx = self._index(key)
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        idx = self._index(key)
        curr = self.table[idx]
        if not curr:
            return

        if curr.key == key:
            self.table[idx] = curr.next
            return
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    assert obj.get(1) == 1
    assert obj.get(3) == -1
    obj.put(2, 1)
    assert obj.get(2) == 1
    obj.remove(2)
    assert obj.get(2) == -1
