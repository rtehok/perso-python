class MyHashSetV1:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        if key not in self.arr:
            self.arr.append(key)

    def remove(self, key: int) -> None:
        for i, v in enumerate(self.arr):
            if v == key:
                self.arr.pop(i)

    def contains(self, key: int) -> bool:
        return key in self.arr


class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for i, k in enumerate(bucket):
            if k == key:
                return
        bucket.append(key)

    def remove(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for i, k in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    def contains(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for k in bucket:
            if k == key:
                return True
        return False


if __name__ == "__main__":
    h = MyHashSet()
    h.add(1)
    h.add(2)
    assert h.contains(1)
    assert not h.contains(3)
    h.add(2)
    h.remove(2)
    assert not h.contains(2)
