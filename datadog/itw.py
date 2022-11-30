import math
from collections import defaultdict
from typing import List


# create buckets from array
def to_buckets(arr: List[int], window_size: int, window_number: int):
    d = defaultdict(int)
    for x in arr:
        key = x // window_size
        if key >= window_number:
            key = window_number
        d[key] += 1

    res = dict(d)
    print(res)

    for k in range(window_number):
        start = k * window_size if k != 0 else 0
        end = start + window_size - 1 if k != window_number - 1 else math.inf
        if end == math.inf:
            print(f"{start}+ : {d[k] + d[window_number]}")
        else:
            print(f"{start} - {end} : {d[k]}")

    return res


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


# fill array by linking points to one another
def interpolate(arr: List[Point], interval: int):
    res = []
    for i in range(len(arr)):
        x2, y2 = arr[i].x, arr[i].y
        x1, y1 = arr[i - 1].x, arr[i - 1].y

        a = (y2 - y1) / (x2 - x1)
        for t in range(x1, x2, interval):
            b = ((x2 * y1) - (x1 * y2)) / (x2 - x1)
            new_y = t * a + b
            res.append(Point(t, new_y))

    res.append(arr[-1])

    return res


if __name__ == "__main__":
    assert to_buckets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 4) == {0: 1, 1: 2, 2: 2, 3: 2, 4: 3}
    assert to_buckets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 4)
    assert to_buckets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 3)
    res = interpolate([Point(1, 1), Point(2, 2), Point(5, 5), Point(6, 4), Point(7, 3), Point(10, 8), Point(11, 9)], 1)
    assert str([str(p) for p in res]) == \
           """['(1, 1.0)', '(2, 2.0)', '(3, 3.0)', '(4, 4.0)', '(5, 5.0)', '(6, 4.0)', '(7, 3.0000000000000018)', '(8, 4.666666666666668)', '(9, 6.333333333333334)', '(10, 8.0)', '(11, 9)']"""
