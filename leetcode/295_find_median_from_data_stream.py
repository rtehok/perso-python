import heapq


class MedianFinder:

    def __init__(self):
        self.heap_max = []  # left (first half, need to have the max)
        self.heap_min = []  # right (second half, need to have the min)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap_max, -num)  # to have the max, multiply by -1
        pop_val = heapq.heappop(self.heap_max)
        heapq.heappush(self.heap_min, -pop_val)  # set in heap_min the opposite value

        if len(self.heap_max) < len(self.heap_min):
            tmp = heapq.heappop(self.heap_min)
            heapq.heappush(self.heap_max, -tmp)  # put it back to heap_min

    def findMedian(self) -> float:
        if len(self.heap_min) == len(self.heap_max):
            a = -self.heap_max[0]
            b = self.heap_min[0]
            return (a + b) / 2

        return -self.heap_max[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
