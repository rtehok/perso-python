from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1

        degree.sort()

        value = 1
        total_importance = 0

        for d in degree:
            total_importance += d * value
            value += 1

        return total_importance


assert Solution().maximumImportance(n=5, roads=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]) == 43
assert Solution().maximumImportance(n=5, roads=[[0, 3], [2, 4], [1, 3]]) == 20
