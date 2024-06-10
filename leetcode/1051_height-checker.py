from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        ans = 0
        for i, h in enumerate(heights):
            if h != sorted_heights[i]:
                ans += 1

        return ans


assert Solution().heightChecker([1, 1, 4, 2, 1, 3]) == 3
assert Solution().heightChecker([5, 1, 2, 3, 4]) == 5
assert Solution().heightChecker([1, 2, 3, 4, 5]) == 0
