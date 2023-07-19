from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        k = float("-inf")

        for x, y in intervals:
            if x >= k:
                k = y
            else:
                ans += 1

        return ans


if __name__ == "__main__":
    assert Solution().eraseOverlapIntervals(intervals=[[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == 2
    assert Solution().eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert Solution().eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]) == 2
    assert Solution().eraseOverlapIntervals(intervals=[[1, 2], [2, 3]]) == 0
