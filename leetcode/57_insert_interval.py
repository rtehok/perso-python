from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        res = []
        for i, (start, end) in enumerate(intervals):
            new_start, new_end = new_interval[0], new_interval[1]
            if new_end < start:
                res.append(new_interval)
                return res + intervals[i:]
            elif new_start > end:
                res.append([start, end])
            else:
                new_interval = [min(new_start, start), max(new_end, end)]

        res.append(new_interval)
        return res


if __name__ == "__main__":
    assert Solution().insert([], [5, 7]) == [[5, 7]]
    assert Solution().insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
