from typing import List


class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        start = None
        end = None
        for val in sorted(list(self.nums)):
            if start is None:
                start = val
                end = val
            elif val - end == 1:
                end = val
            else:
                intervals.append([start, end])
                start = end = val
        if start is not None:
            intervals.append([start, end])
        return intervals


if __name__ == "__main__":
    s = SummaryRanges()
    s.addNum(1)
    print(s.getIntervals())
    s.addNum(3)
    print(s.getIntervals())
    s.addNum(7)
    print(s.getIntervals())
    s.addNum(2)
    print(s.getIntervals())
    s.addNum(6)
    print(s.getIntervals())
