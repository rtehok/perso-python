from typing import List


class Solution:
    def mergeV1(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key=lambda x: x[0])

        n = len(intervals)

        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            current_start, current_end = intervals[i][0], intervals[i][1]
            if current_start <= end:
                end = max(current_end, end)
            else:
                res.append([start, end])
                start = current_start
                end = current_end

        res.append([start, end])

        return res

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        intervals.sort(key=lambda x: x[0])

        for start, end in intervals:
            if not merged or merged[-1][1] < start:  # no overlap
                merged.append([start, end])
            else:  # update the end
                merged[-1][1] = max(merged[-1][1], end)

        return merged


if __name__ == "__main__":
    assert Solution().merge([[1, 4], [0, 2], [3, 5]]) == [[0, 5]]
    assert Solution().merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]
