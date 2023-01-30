import collections


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        # data structure 1: dictionary which maps key to count
        # maps key to (value, count) pair
        self.cache_key = dict()
        # data structure 2: dictionary which maps count to a orderedDict
        # maps count to an OrderedDict which maintains key, value pairs
        self.cache_orderedCount = dict()
        self.min_cnt = 0

    def _updateCacheCountDict(self, key, value, new_cnt):
        if new_cnt not in self.cache_orderedCount:
            self.cache_orderedCount[new_cnt] = collections.OrderedDict()

        self.cache_orderedCount[new_cnt][key] = value
        self.cache_orderedCount[new_cnt].move_to_end(key)

    def get(self, key: int) -> int:
        val = -1

        if key in self.cache_key:
            val, old_cnt = self.cache_key[key]
            self.cache_key[key][1] += 1  # increment old count for key
            del self.cache_orderedCount[old_cnt][key]  # delete before update
            new_cnt = self.cache_key[key][1]
            self._updateCacheCountDict(key, val, new_cnt)
            if self.min_cnt == old_cnt and len(self.cache_orderedCount[old_cnt]) == 0:
                self.min_cnt = new_cnt

        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache_key:
            self.cache_key[key][0] = value
            old_cnt = self.cache_key[key][1]
            self.cache_key[key][1] += 1
            new_cnt = old_cnt + 1
            del self.cache_orderedCount[old_cnt][key]
            self._updateCacheCountDict(key, value, new_cnt)
            if self.min_cnt == old_cnt and len(self.cache_orderedCount[old_cnt]) == 0:
                self.min_cnt = new_cnt
        else:
            if self.used < self.capacity:
                self.used += 1
            else:
                rm_key, rm_val = self.cache_orderedCount[self.min_cnt].popitem(0)
                del self.cache_key[rm_key]

            self.cache_key[key] = [value, 1]
            self._updateCacheCountDict(key, value, 1)
            self.min_cnt = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
    s = LFUCache(2)
    s.put(1, 1)
    s.put(2, 2)
    print(s.get(1))
    s.put(3, 3)
    print(s.get(2))
    print(s.get(3))
    s.put(4, 4)
    print(s.get(1))
    print(s.get(3))
    print(s.get(4))
