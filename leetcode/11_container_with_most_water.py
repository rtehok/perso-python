from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def loop(first, last, res):
            if first == last:
                return res

            area = min(height[first], height[last]) * (last - first)
            if height[first] > height[last]:
                return loop(first, last - 1, max(area, res))
            else:
                return loop(first + 1, last, max(area, res))

        return loop(0, len(height) - 1, 0)


if __name__ == "__main__":
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 1]) == 1
