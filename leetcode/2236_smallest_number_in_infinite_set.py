import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.is_present = set()
        self.added_integers = []
        self.current_integer = 1

    def popSmallest(self) -> int:
        if len(self.added_integers):
            value = heapq.heappop(self.added_integers)
            self.is_present.remove(value)
        else:
            value = self.current_integer
            self.current_integer += 1

        return value

    def addBack(self, num: int) -> None:
        if self.current_integer <= num or num in self.is_present:
            return
        heapq.heappush(self.added_integers, num)
        self.is_present.add(num)


if __name__ == "__main__":
    obj = SmallestInfiniteSet()
    obj.addBack(2)
    assert obj.popSmallest() == 1
    assert obj.popSmallest() == 2
    assert obj.popSmallest() == 3
    obj.addBack(1)
    assert obj.popSmallest() == 1
    assert obj.popSmallest() == 4
    assert obj.popSmallest() == 5
